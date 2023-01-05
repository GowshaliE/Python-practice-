import csv
import xmltodict
import pandas as pd

with open('/home/gowshali/Downloads/IE000Q2P3ZQ3.xls','r', encoding='utf-8') as csvfile:
    filedata = csvfile.read()


data_dict = xmltodict.parse(csvfile)
data_dict = data_dict['root']['worksheet'][1]['Row']
fieldnames = ['S.No','As Of','Currency','NAV','Securities In Issue','Net Assets','Fund Return Series','Benchmark Return Series']
fields = []
for column in data_dict:
    fields.append({
        "S.No": column['@index'],
        "As Of": column['As_Of_date'],
        "Currency": column['Currency'],
        "NAV": column['NAV'],
        "Securities In Issue": column['Securities_In_Issue'],
        "Net Assets": column['Net_Assets'],
        "Fund Return Series": column['Fund_Return_Series'],
        "Benchmark Return Series": column['BenchmarkReturnSeries'],
    })

with open('xmloutput2.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for field in fields:
        writer.writerow(field)