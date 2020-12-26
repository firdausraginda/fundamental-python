# reference: https://openpyxl.readthedocs.io/en/stable/styles.html

import openpyxl
from openpyxl.styles import *

# setting excel file, worksheet, & cell
workbook = openpyxl.load_workbook("./Employees.xlsx")
sheet = workbook['EmployeeData']
cell = sheet['B8']

# setting up font style
fontStyle = Font(color='00FFCC00', bold=True, italic=True)
cell.font = fontStyle  # implement font style

# setting up background color
backgroundStyle = PatternFill(fill_type='solid', bgColor='F7FE2E')
cell.fill = backgroundStyle  # implement background style

# setting up border style
borderStyle = Border(left=Side(border_style='double', color='322FEC'),
                     right=Side(border_style='double', color='322FEC'),
                     top=Side(border_style='double', color='322FEC'),
                     bottom=Side(border_style='double', color='322FEC')
                     )
cell.border = borderStyle # implement border style

# setting up alignment style
alignStyle = Alignment(horizontal = 'left')
cell.alignment = alignStyle # implement aligntment style

workbook.save('./Employees.xlsx')