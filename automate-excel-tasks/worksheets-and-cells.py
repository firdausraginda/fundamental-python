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

# ----------------------------------------------------------

# GETTING GENERAL INFORMATION ABOUT THE SHEET

# select sheet
# sheet = workbook['EmployeeData']

# print(sheet.title) # print current active sheet title
# print(sheet.active_cell) # print current active cell
# print(sheet.dimensions) # print cell contains value in sheet
# print(sheet.max_row) # print number of rows
# print(sheet.max_column) # print number of column

# ----------------------------------------------------------

# PRINT CELL VALUE & DATA TYPE

# print sheet values in form of tuples
# for i in sheet.values:
#     print(i)

# get a value of a cell using cell cordinate
# valueCell = sheet['B7'].value
# print(valueCell)

# get a value of a cell by specifying row & column separately
# valueCell2 = sheet.cell(row = 6, column = 2).value
# print(valueCell2)

# print data type of a value inside the cell
# valueCell3 = sheet.cell(row = 6, column = 2)
# print(valueCell3.data_type)

# get sheet of a cell
# cell = sheet['C4']
# print(cell.parent) # print parent sheet of a cell

# ----------------------------------------------------------

# CHANGE VALUE INSIDE A CELL

# cell = sheet['B2']
# print(cell.value) # print current value
# cell.value = 'Mihai'
# workbook.save('./Employees.xlsx')
# print(cell.value) # print value after made changes