#ライブラリを取り込む
import openpyxl as excel
import os

cd = os.getcwd()

#新規ワークブックを作る
book = excel.Workbook()

#アクティブなワークシートを生成
sheet = book.active

#A1のセルに値を入力
sheet["A1"] = "こんにちは"

#ファイルを名前を付けて保存
book.save(cd + "\\Python project\\Excel project\\Hello.xlsx")