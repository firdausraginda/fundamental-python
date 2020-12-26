# reference: https://openpyxl.readthedocs.io/en/stable/index.html

# import openpyxl

# define excel file
# workbook = openpyxl.load_workbook("./Employees.xlsx")

# print(workbook.properties) # get excel properties
# print(workbook.sheetnames) # get excel sheetnames

# create sheet
# workbook.create_sheet('TestSheet')
# workbook.save('./Employees.xlsx')

# delete sheet
# sheet = workbook['TestSheet']
# workbook.remove(sheet)
# workbook.save('./Employees.xlsx')

# getting general information about the sheet
# sheet = workbook['EmployeeData']
# print(sheet.title) # print current active sheet title
# print(sheet.active_cell) # print current active cell
# print(sheet.dimensions) # print cell contains value in sheet
# print(sheet.max_row) # print number of rows
# print(sheet.max_column) # print number of column

# print sheet values in form of tuples
# for i in sheet.values:
#     print(i)

