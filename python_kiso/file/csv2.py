# -*- coding: utf-8 -*-
import csv

# ファイルオープン
#f = open('output.csv', 'w')
#writer = csv.writer(f, lineterminator='\n')

# ファイルを書き込みモードでオープン
with open('sample.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
#    writer = csv.writer(f)  # writerオブジェクトを作成

#    writer.writerow(header) # ヘッダーを書き込む
#    writer.writerows(body)  # 内容を書き込む
  
    # データをリストに保持
    csvlist = []
    csvlist.append("hoge")
    csvlist.append("fuga")
    
    # 出力
    writer.writerow(csvlist)
    
    # ファイルクローズ
    f.close()
