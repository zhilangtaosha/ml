# -*- coding: utf-8 -*-

import csv

# ヘッダー
header = ['ID', 'name']

# 内容
body = [
  [0, 'Alex'],
  [1, 'John'],
  [2, 'Bob']
]

# ファイルを書き込みモードでオープン
with open('sample.csv', 'w') as f:

  writer = csv.writer(f)  # writerオブジェクトを作成
  writer.writerow(header) # ヘッダーを書き込む
  writer.writerows(body)  # 内容を書き込む