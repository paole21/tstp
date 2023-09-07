import openpyxl as excel
import os

cd = os.getcwd()

book = excel.load_workbook(cd + "\\Python project\\Excel project\\Hello.xlsx")

sheet = book.worksheets[0]
#方法2、book.activesheet:最後に開いたシート
#方法3、book["シート名"]

cell = sheet["A1"]

print(cell.value)