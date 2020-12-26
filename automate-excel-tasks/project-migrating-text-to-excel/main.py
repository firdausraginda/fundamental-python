from openpyxl import Workbook
from openpyxl.styles import *
from openpyxl.worksheet.table import Table, TableStyleInfo

text_file = open('./employees.txt')
records = []

text_file.seek(0) # set the cursor at the very beginning

# read txt file per lines in list form and append to records list
for record in text_file.readlines():
    records.append(record.rstrip('\n').split(';'))

# create workbook / excel file
workbook = Workbook()
file_path = './MyCompanyStaff.xlsx'
workbook.save(file_path)

# rename default sheet
sheet = workbook['Sheet']
sheet.title = 'Employees'

# migrating data to sheet
for row in records:
    sheet.append(row)

# setting up table style
tableRange = Table(displayName='Table', ref='A1:G11') # cordinate A1:G11 based on 7 columns & 11 rows
tableStyle = TableStyleInfo(name='TableStyleMedium9', showRowStripes=True, showColumnStripes=True) # use pre-defined table style
tableRange.tableStyleInfo = tableStyle # implement table style to table with specified range
sheet.add_table(tableRange) # add table to sheet

# setting up font style for salary > 55000
fontStyle = Font(color='FF0000', bold=True, italic=True)

# implement font style for salary column
for cell_no in range(2, 12):
    if int(sheet['G%s' % (cell_no)].value) > 55000:
        sheet['G%s' % (cell_no)].font = fontStyle

workbook.save(file_path)
text_file.close()