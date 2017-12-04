# Crashの発生頻度を示す.csvファイルをユーザごとにまとめる

import csv
import re

def output_csv(ary):
    # ファイルを書き込みモードでオープン
    with open('user_data.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')

        # 出力
        writer.writerows(ary)  # 内容を書き込む
        # ファイルクローズ
        f.close()

#2017-08-21 11:53:35Z
dateReg = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')
def is_timing(s):
    return dateReg.match(s) is not None

#INDONESIA01\RYOSUZUKI
userReg = re.compile(r'^INDONESIA01')
def is_user(s):
    return userReg.match(s) is not None

#INNHOST065
vdiReg = re.compile(r'^INNHOST')
def is_vdi(s):
    return vdiReg.match(s) is not None

#項目をまとめる
def sort_ary(ary):

    tmp_ary = []
    update_ary = []
    for a in ary:
        tmp_ary.append(a)

        if is_vdi(a):
            update_ary.append(tmp_ary)
            tmp_ary = []

    return update_ary

#####################
# Main
ary = []
tmp_ary = []
i = 0

f = open('addin_crash_info.txt')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines: リスト。要素は1行の文字列データ
for line in lines:
    line = line.replace('\n','')

    #判定
    #2017-08-21 11:53:35Z
    if is_timing(line):
        tmp_ary.append(line)

    #INDONESIA01\MFIRMAN
    elif is_user(line):
        tmp_ary.append(line)

    #INNVDIHOST065
    elif is_vdi(line):
        tmp_ary.append(line)

    else:
        continue

    i+=1

output_csv(sort_ary(tmp_ary))
print("done")
