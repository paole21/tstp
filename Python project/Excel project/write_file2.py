import openpyxl as excel
import os
import datetime

cd = os.getcwd()
cd = cd + "\\Python project\\Excel project\\Year_age.xlsx"

book = excel.load_workbook(cd)
sheet = book.worksheets[0]

#年度を得る
thisyear = datetime.date.today().year

for i in range(80):
    sheet.cell(row=i+1, column=1, value=str(thisyear-i) +"年")
    sheet.cell(row=i+1, column=2, value=str(i) +"歳")

book.save(cd)