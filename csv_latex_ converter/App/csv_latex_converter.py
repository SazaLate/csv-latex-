#ライブラリ置き場
import pandas as pd
import csv #Pythonでcsvを扱うためのライブラリ
import glob #ファイル検索をするライブラリ
import os
import re
import pprint

result = []
with open("sample1.csv",'rt',encoding = "utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        result.append(row)
        
#ヘッダーを抽出
header = result.pop(0)


#列指定を入れるl or c or r
#空要素がないリストを検索
list_num = 0 #最大の要素数を持っている行に対応させる
for i in result:
    list_example =  [a for a in i if a != '']
    if len(list_example) > list_num:
        list_num = len(list_example)
    
#list_num #最終的な列の数
column_des = []
print("これから列指定を行います")
print("l:左寄せ，c:中央寄せ,r:右寄せ,p{hogehoge cm}:列の大きさ指定")
for designation in range(list_num):
    column = input(str(designation + 1)  + '列目の指定は：')
    column_des.append(column)

#column_des　列指定

#罫線ありかなしか
rule_plus = []
ruled_line = input("縦の罫線は必要ですかY/N:")
if ruled_line == "Y":
    for rule in column_des:
        rule_plus.append(str(rule + "|"))
    rule_plus.insert(0,"|")

ruled_column = "".join(rule_plus)


#キャプションを付ける
caption_need = input("表にキャプションはつけますか？Y/N:")
if caption_need == "Y":
    caption = input("キャプションを入力してください")

#参照を付ける
ref_need = input("表に参照はつけますか？Y/N:")
if ref_need == "Y":
    refarence = input("参照を入力してください")

#表のセンタリングの有無
center_need = input("表のセンタリングをしますか？Y/N:\n")


#表示
print("csvをlatexに変換中…")
print("\\begin{table}[htbp]")
if center_need == "Y":
    print("\\centering")
if caption_need == "Y":
    print("\\caption{"+ caption +"}")
print("\t\\begin{tabular}{"+ ruled_column + "}")
#ここから中身
#ヘッダー
header_latex = ' & ' .join(header)
print("\t\t" + header_latex + "\\\\\\hline\hline")
#要素
for table in result:
    result_latex = ' & ' .join(table)
    print("\t\t" + result_latex + "\\\\\\hline")
#ここまで中身
print("\t\\end{tabular}")
if ref_need == "Y":
    print("\\label{"+ refarence +"}")
print("\\end{table}\n")


print("文中参照用のタグ：\\ref{"+ refarence + "}")
