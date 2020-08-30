from pandas import ExcelWriter
import csv
import pandas as pd


file_errors_location = '/Users/user/Downloads/contacts.xlsx'
df = pd.read_excel(file_errors_location)
emails = df['E-mail 1 - Value']  # emails col

Names = []
Companies = []

words = ['Gmail'
         'pwc'
         'EY'
         'KPMG'
         'Vulcan'
         'Jobs'
         'Info'
         'Hiring', 'hr'
         ]

for row in emails:
    if any(e in row for e in words):
        Names.append("")
        Companies.append("")
    else:
        name, compamnyCom = row.split('@')
        name = name.replace(".", " ")  # for ex of adi.persiko
        Names.append(name)
        Companies.append(compamnyCom.split('.')[0])
df['Company'] = Companies
df['Names'] = Names
writer = ExcelWriter(file_errors_location)
df.to_excel(writer, 'Sheet1')
writer.save()
