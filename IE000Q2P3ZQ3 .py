import csv
import xmltodict
import pandas as pd

fields = []
def convertxml_todict():
    with open('/home/gowshali/Desktop/gitlab/tivona-explorer/gowshali/IE000Q2P3ZQ3.xml','r', encoding='utf-8') as csvfile:
        filedata = csvfile.read()
        
        data_dict = xmltodict.parse(filedata)
        data_dict = data_dict['root']['worksheet'][1]['Row']
       
        
        for column in data_dict:
            fields.append({
                "S.No": column['Index'],
                "As Of": column['AsOf'],
                "Currency": column['Currency'],
                "NAV": column['NAV'],
                "Securities In Issue": column['SecuritiesInIssue'],
                "Net Assets": column['NetAssets'],
                "Fund Return Series": column['FundReturnSeries'],
                "Benchmark Return Series": column['BenchmarkReturnSeries'],
            })
            return filedata,fields
def writing_tocsv(convertxml_todict):   
         
    with open('xmloutput.csv', 'w', newline='') as csvfile:
            
            fieldname= ['S.No','As Of','Currency','NAV','Securities In Issue','Net Assets','Fund Return Series','Benchmark Return Series']
            writer = csv.DictWriter(csvfile, fieldnames=fieldname)
            writer.writeheader()
            for row in fields:
                writer.writerow(row)
writing_tocsv(convertxml_todict)                


  
         