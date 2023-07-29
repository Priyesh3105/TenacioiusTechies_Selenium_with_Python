import openpyxl

path = "C:\\Users\\HP\\Documents\\test.xlsx"

workbook=openpyxl.load_workbook(path)

sheet = workbook.active


for r in range(1, 20):
    for c in range(1, 10):
        sheet.cell(row=r,column=c).value = "hello world"


workbook.save(path)