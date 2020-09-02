import csv
# Load the Pandas libraries with alias 'pd'
import pandas as pd

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Facebook Posts").sheet1  # Open the spreadhseet
# sheet = client.open("Yuval Beiser Leads").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

# row = sheet.row_values(3)  # Get a specific row
df_emails = sheet.col_values(3)  # Get a specific column

#df = pd.read_csv('FacebookPosts.csv', header=None)

Hr_Companies = set(['CV-Naor.peeri@ls-techs.com', 'Jennyb@elipse-eng.com', 'Job@in-touch.co.il', 'Jobs@Net-Bet.net',
                    'Kenigsman.eli.jobs@gmail.com', 'jobs', 'anatlz@sela.co.il', 'apply.37.81B@applynow.io', 'neta@gtech.co.il', 'adiya@bpsoft.co.il', 'shayleek@be2see.co.il', 'Ofir.Goldberg@ness-tech.co.il', 'Ortal.E@top-soft.co.il', 'hr.team@herolo.co.il',
                    'sqlink', 'herolo', 'malam', 'aman', 'Hiring', 'hr', "8200ac", "devalore", "asperii",
                    "log-on", "intuit", "odin-team", "ictbit", "peeri",
                    "ls-techs", "applynow", "esr", "cps", "be2see", "sqlink",
                    "hitech", "experis", "compie", "elipse-eng",
                    "malam", "datacube",
                    "sela", "one1", "spread-out", "matrix"
                    ])
s = set()

#all_emails = set(x[2:-2] for x in df[2])

s = set([x[2:-2] for x in df_emails if not any(e in x for e in Hr_Companies)])
# s.remove('[]')
