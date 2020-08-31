from pandas import ExcelWriter
import csv
import pandas as pd

file_errors_location = '/Users/user/PycharmProjects/soldgame/fun/Alumni-Codes/FacebookPosts.xlsx'
df = pd.read_excel(file_errors_location)
emails = df["Emails"]
final_emails = []

emails= list(set(emails)) # remove duplicates

Names = []
Companies = []

forbiden_words = ['Gmail'
                  'pwc'
                  'EY'
                  'KPMG'
                  'Vulcan'
                  'Jobs'
                  'Info', '8200ac'
                  'Hiring', 'hr', "8200ac", "devalore", "asperii",
                  "log-on", "intuit", "odin-team", "ictbit", "peeri",
                  "ls-techs", "applynow", "esr", "cps", "be2see", "sqlink",
                  "hitech", "experis", "compie", "elipse-eng",
                  "malam", "datacube",
                  "sela", "one1", "spread-out", "matrix"
                  ]


for row2 in emails:
    row= row2[2:-2]
    if row=="":
        continue
    if isinstance(row, float) :
        continue
    if any(e in row for e in forbiden_words) :
        # final_emails.append("")
        continue
    else:
        final_emails.append(row)
        name, compamnyCom = row.split('@')
        name = name.replace(".", " ")  # for ex of adi.persiko
        Names.append(name)
        company_name = compamnyCom.split('.')[0]
        if company_name=="gmail" : 
            company_name=" "
        Companies.append(company_name)

path_final = '/Users/user/PycharmProjects/soldgame/fun/Alumni-Codes/FaceEmails.xlsx'
df2 = pd.read_excel(path_final)

df2['emails']= final_emails
df2['Company'] = Companies
df2['Names'] = Names
#df["final"] = final_emails
writer = ExcelWriter(path_final)
df2.to_excel(writer, 'Sheet1')
writer.save()