
## method 1
import xlrd

# Open the Workbook
workbook = xlrd.open_workbook("/home/gowshali/Documents/files/IE000QOU09J7.xls")

# Open the worksheet
worksheet = workbook.sheet_by_index(0)

## method 2
    
from openpyxl import load_workbook
from yattag import Doc, indent
  

wb = load_workbook("/home/gowshali/Documents/files/IE000QOU09J7.xls")
ws = wb.worksheets[0]
  

doc, tag, text = Doc().tagtext()
  
xml_header = '<?xml version="1.0" encoding="UTF-8"?>'

  

doc.asis(xml_header)

