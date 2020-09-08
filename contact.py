from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from pandas import ExcelWriter
import csv
import pandas as pd

path = '/Users/user/PycharmProjects/soldgame/fun/Alumni-Codes/FaceEmails.xlsx'
file_errors_location = 'FacebookPosts.xlsx'
df = pd.read_excel(file_errors_location)
emails = df['Emails']  # emails col

Names = []
Companies = []
Final_emails = []

words = ['Gmail', 'cv'
         'pwc', 'ess',
                  'EY',
                  'KPMG',
                  'Vulcan',
                  'Jobs',  'job',
                  'Info', '8200ac',
                  'Hiring', 'hr', "8200ac", "devalore", "asperii",
                  "log-on", "intuit", "odin-team", "ictbit", "peeri",
                  "ls-techs", "applynow", "esr", "cps", "be2see", "sqlink",
                  "hitech", "experis", "compie", "elipse-eng",
                  "malam", "datacube",
                  "sela", "one1", "spread-out", "matrix", 'logica'
         ]

emails = list(set(emails))
emails.remove('Emails')
emails.remove('[]')


for row in emails:
    row = row[2:-2]
    if any(e in row for e in words) or row.count('@') > 1:
        continue
        Names.append("")
        Companies.append("")
    else:
        name, compamnyCom = row.split('@')
        name = name.replace(".", " ")  # for ex of adi.persiko
        Names.append(name)
        Companies.append(compamnyCom.split('.')[0])
        Final_emails.append(row)

df = pd.read_excel(path)

df['Company'] = Companies
df['Names'] = Names
df['emails'] = Final_emails
writer = ExcelWriter(path)
df.to_excel(writer, 'Sheet1')
writer.save()

# ----------------------------------------------------
# Write to Excel - Yuval Beiser Leads

# Load the Pandas libraries with alias 'pd'

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Yuval Beiser Leads").sheet1  # Open the spreadhseet
k = 77
for i in range(len(Names)):
    sheet.update_cell(i+k, 9, Names[i])  # names_f
    sheet.update_cell(i+k, 8, Final_emails[i])  # emails_f
    sheet.update_cell(i+k, 7, Companies[i])  # emails_f
