from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import mean_squared_error,r2_score
import time
#%matplotlib inline

import xgboost
from bayes_opt import BayesianOptimization

import warnings
warnings.filterwarnings("ignore")

"""
Contributions from:
DSEverything - Mean Mix - Math, Geo, Harmonic (LB 0.493)
https://www.kaggle.com/dongxu027/mean-mix-math-geo-harmonic-lb-0-493
JdPaletto - Surprised Yet? - Part2 - (LB: 0.503)
https://www.kaggle.com/jdpaletto/surprised-yet-part2-lb-0-503
hklee - weighted mean comparisons, LB 0.497, 1ST
https://www.kaggle.com/zeemeen/weighted-mean-comparisons-lb-0-497-1st

Also all comments for changes, encouragement, and forked scripts rock

Keep the Surprise Going
"""

import glob, re
import numpy as np
import pandas as pd
from sklearn import *
from datetime import datetime
from xgboost import XGBRegressor
import h2o
from h2o.automl import H2OAutoML
h2o.init()

"""
Contributions from:
DSEverything - Mean Mix - Math, Geo, Harmonic (LB 0.493)
https://www.kaggle.com/dongxu027/mean-mix-math-geo-harmonic-lb-0-493
JdPaletto - Surprised Yet? - Part2 - (LB: 0.503)
https://www.kaggle.com/jdpaletto/surprised-yet-part2-lb-0-503
hklee - weighted mean comparisons, LB 0.497, 1ST
https://www.kaggle.com/zeemeen/weighted-mean-comparisons-lb-0-497-1st

Also all comments for changes, encouragement, and forked scripts rock

Keep the Surprise Going
"""

import glob, re
import numpy as np
import pandas as pd
from sklearn import *
from datetime import datetime
from xgboost import XGBRegressor

data = {
    'tra': pd.read_csv('../../../mltestdata/05_recruit/air_visit_data.csv'),
    'as': pd.read_csv('../../../mltestdata/05_recruit/air_store_info.csv'),
    'hs': pd.read_csv('../../../mltestdata/05_recruit/hpg_store_info.csv'),
    'ar': pd.read_csv('../../../mltestdata/05_recruit/air_reserve.csv'),
    'hr': pd.read_csv('../../../mltestdata/05_recruit/hpg_reserve.csv'),
    'id': pd.read_csv('../../../mltestdata/05_recruit/store_id_relation.csv'),
    'tes': pd.read_csv('../../../mltestdata/05_recruit/sample_submission.csv'),
    'hol': pd.read_csv('../../../mltestdata/05_recruit/date_info.csv').rename(columns={'calendar_date':'visit_date'})
    }

data['hr'] = pd.merge(data['hr'], data['id'], how='inner', on=['hpg_store_id'])

for df in ['ar','hr']:
    data[df]['visit_datetime'] = pd.to_datetime(data[df]['visit_datetime'])
    data[df]['visit_datetime'] = data[df]['visit_datetime'].dt.date
    data[df]['reserve_datetime'] = pd.to_datetime(data[df]['reserve_datetime'])
    data[df]['reserve_datetime'] = data[df]['reserve_datetime'].dt.date
    data[df]['reserve_datetime_diff'] = data[df].apply(lambda r: (r['visit_datetime'] - r['reserve_datetime']).days, axis=1)
    tmp1 = data[df].groupby(['air_store_id','visit_datetime'], as_index=False)[['reserve_datetime_diff', 'reserve_visitors']].sum().rename(columns={'visit_datetime':'visit_date', 'reserve_datetime_diff': 'rs1', 'reserve_visitors':'rv1'})
    tmp2 = data[df].groupby(['air_store_id','visit_datetime'], as_index=False)[['reserve_datetime_diff', 'reserve_visitors']].mean().rename(columns={'visit_datetime':'visit_date', 'reserve_datetime_diff': 'rs2', 'reserve_visitors':'rv2'})
    data[df] = pd.merge(tmp1, tmp2, how='inner', on=['air_store_id','visit_date'])

data['tra']['visit_date'] = pd.to_datetime(data['tra']['visit_date'])
data['tra']['dow'] = data['tra']['visit_date'].dt.dayofweek
data['tra']['year'] = data['tra']['visit_date'].dt.year
data['tra']['month'] = data['tra']['visit_date'].dt.month
data['tra']['visit_date'] = data['tra']['visit_date'].dt.date

data['tes']['visit_date'] = data['tes']['id'].map(lambda x: str(x).split('_')[2])
data['tes']['air_store_id'] = data['tes']['id'].map(lambda x: '_'.join(x.split('_')[:2]))
data['tes']['visit_date'] = pd.to_datetime(data['tes']['visit_date'])
data['tes']['dow'] = data['tes']['visit_date'].dt.dayofweek
data['tes']['year'] = data['tes']['visit_date'].dt.year
data['tes']['month'] = data['tes']['visit_date'].dt.month
data['tes']['visit_date'] = data['tes']['visit_date'].dt.date

unique_stores = data['tes']['air_store_id'].unique()
stores = pd.concat([pd.DataFrame({'air_store_id': unique_stores, 'dow': [i]*len(unique_stores)}) for i in range(7)], axis=0, ignore_index=True).reset_index(drop=True)

#sure it can be compressed...
tmp = data['tra'].groupby(['air_store_id','dow'], as_index=False)['visitors'].min().rename(columns={'visitors':'min_visitors'})
stores = pd.merge(stores, tmp, how='left', on=['air_store_id','dow'])
tmp = data['tra'].groupby(['air_store_id','dow'], as_index=False)['visitors'].mean().rename(columns={'visitors':'mean_visitors'})
stores = pd.merge(stores, tmp, how='left', on=['air_store_id','dow'])
tmp = data['tra'].groupby(['air_store_id','dow'], as_index=False)['visitors'].median().rename(columns={'visitors':'median_visitors'})
stores = pd.merge(stores, tmp, how='left', on=['air_store_id','dow'])
tmp = data['tra'].groupby(['air_store_id','dow'], as_index=False)['visitors'].max().rename(columns={'visitors':'max_visitors'})
stores = pd.merge(stores, tmp, how='left', on=['air_store_id','dow'])
tmp = data['tra'].groupby(['air_store_id','dow'], as_index=False)['visitors'].count().rename(columns={'visitors':'count_observations'})
stores = pd.merge(stores, tmp, how='left', on=['air_store_id','dow'])

stores = pd.merge(stores, data['as'], how='left', on=['air_store_id'])
# NEW FEATURES FROM Georgii Vyshnia
stores['air_genre_name'] = stores['air_genre_name'].map(lambda x: str(str(x).replace('/',' ')))
stores['air_area_name'] = stores['air_area_name'].map(lambda x: str(str(x).replace('-',' ')))
lbl = preprocessing.LabelEncoder()
for i in range(10):
    stores['air_genre_name'+str(i)] = lbl.fit_transform(stores['air_genre_name'].map(lambda x: str(str(x).split(' ')[i]) if len(str(x).split(' '))>i else ''))
    stores['air_area_name'+str(i)] = lbl.fit_transform(stores['air_area_name'].map(lambda x: str(str(x).split(' ')[i]) if len(str(x).split(' '))>i else ''))
stores['air_genre_name'] = lbl.fit_transform(stores['air_genre_name'])
stores['air_area_name'] = lbl.fit_transform(stores['air_area_name'])

data['hol']['visit_date'] = pd.to_datetime(data['hol']['visit_date'])
data['hol']['day_of_week'] = lbl.fit_transform(data['hol']['day_of_week'])
data['hol']['visit_date'] = data['hol']['visit_date'].dt.date
train = pd.merge(data['tra'], data['hol'], how='left', on=['visit_date'])
test = pd.merge(data['tes'], data['hol'], how='left', on=['visit_date'])

train = pd.merge(train, stores, how='left', on=['air_store_id','dow'])
test = pd.merge(test, stores, how='left', on=['air_store_id','dow'])

for df in ['ar','hr']:
    train = pd.merge(train, data[df], how='left', on=['air_store_id','visit_date'])
    test = pd.merge(test, data[df], how='left', on=['air_store_id','visit_date'])

train['id'] = train.apply(lambda r: '_'.join([str(r['air_store_id']), str(r['visit_date'])]), axis=1)

train['total_reserv_sum'] = train['rv1_x'] + train['rv1_y']
train['total_reserv_mean'] = (train['rv2_x'] + train['rv2_y']) / 2
train['total_reserv_dt_diff_mean'] = (train['rs2_x'] + train['rs2_y']) / 2

test['total_reserv_sum'] = test['rv1_x'] + test['rv1_y']
test['total_reserv_mean'] = (test['rv2_x'] + test['rv2_y']) / 2
test['total_reserv_dt_diff_mean'] = (test['rs2_x'] + test['rs2_y']) / 2

# NEW FEATURES FROM JMBULL
train['date_int'] = train['visit_date'].apply(lambda x: x.strftime('%Y%m%d')).astype(int)
test['date_int'] = test['visit_date'].apply(lambda x: x.strftime('%Y%m%d')).astype(int)
train['var_max_lat'] = train['latitude'].max() - train['latitude']
train['var_max_long'] = train['longitude'].max() - train['longitude']
test['var_max_lat'] = test['latitude'].max() - test['latitude']
test['var_max_long'] = test['longitude'].max() - test['longitude']

# NEW FEATURES FROM Georgii Vyshnia
train['lon_plus_lat'] = train['longitude'] + train['latitude']
test['lon_plus_lat'] = test['longitude'] + test['latitude']

lbl = preprocessing.LabelEncoder()
train['air_store_id2'] = lbl.fit_transform(train['air_store_id'])
test['air_store_id2'] = lbl.transform(test['air_store_id'])

col = [c for c in train if c not in ['id', 'air_store_id', 'visit_date','visitors']]
train = train.fillna(-1)
test = test.fillna(-1)

train['visitors'] = np.log1p(train['visitors'].values)

combine = [train, test]
gw_list = ['2016-04-29','2016-04-30','2016-05-01','2016-05-02','2016-05-03','2016-05-04','2016-05-05','2017-04-29','2017-04-30','2017-05-01','2017-05-02','2017-05-03','2017-05-04','2017-05-05']
post_gw_list=['2016-05-06']
train['gw_flg'] = 0
train['post_gw_flg'] = 0
test['gw_flg'] = 0
test['post_gw_flg'] = 0
update_gw_list = [["0" for i in range(3)] for j in range(len(gw_list))]
update_post_gw_list = [["0" for i in range(3)] for j in range(len(post_gw_list))]

from datetime import date
for index, gw_date in enumerate(gw_list):
    temp_list = gw_date.split("-")
    for col_i, temp_figure in enumerate(temp_list):
        update_gw_list[index][col_i]=int(temp_figure)

    #print("{}  {}  {}".format(update_list[index][0],update_list[index][1],update_list[index][2]))

for index, gw_date in enumerate(post_gw_list):
    temp_list = gw_date.split("-")
    for col_i, temp_figure in enumerate(temp_list):
        update_post_gw_list[index][col_i]=int(temp_figure)

for dataset in combine:
    for index in range(len(update_gw_list)):
        dataset.loc[dataset.visit_date == date(update_gw_list[index][0],update_gw_list[index][1],update_gw_list[index][2]), 'gw_flg'] = 1

for dataset in combine:
    for index in range(len(update_post_gw_list)):
        dataset.loc[dataset.visit_date == date(update_post_gw_list[index][0],update_post_gw_list[index][1],update_post_gw_list[index][2]), 'post_gw_flg'] = 1

drop_cols=['visitors','air_store_id','visit_date','id']
y_train=train['visitors']
x_train=train.drop(drop_cols, axis=1)

x_test=test.copy()
x_test=x_test.drop(drop_cols, axis=1)

#y = train.visitors
train_output = train.visitors
train_input = train.copy()
test_input = test.copy()

drop_cols=['visitors','air_store_id','visit_date','id']
train_input=train_input.drop(drop_cols, axis=1)
test_input=test_input.drop(drop_cols, axis=1)

train_automl = train.drop(['air_store_id','visit_date','id'], axis=1)

train_automl.shape

train_input.shape

test_input.shape

# Modeling

## H2O

#import h2o
#h2o.init()

#h2o.demo("glm")

#h2o.connect()

htrain = h2o.H2OFrame(train_automl)
htest = h2o.H2OFrame(test_input)

#htrain.drop(['id', 'air_store_id', 'visit_date'])
#htest.drop(['id', 'air_store_id', 'visit_date'])

x =htrain.columns
y ='visitors'
x.remove(y)

from h2o.automl import H2OAutoML

def RMSLE(y_, pred):
    return metrics.mean_squared_error(y_, pred)**0.5

print('Starting h2o autoML model!')

#aml = H2OAutoML(max_runtime_secs = 8000)
aml = H2OAutoML()
aml.train(x=x, y =y, training_frame=htrain, leaderboard_frame = htest)
