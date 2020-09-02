import pandas as pd
from pandas import ExcelWriter
import csv

path = '/Users/user/PycharmProjects/soldgame/fun/Alumni-Codes/FaceEmails.xlsx'
df = pd.read_excel(path)

emails = ["emails"]
Companies=["Companies"]
Names=["Names"]

df = df[df['Names'] == '']

#
# df['Company'] = Companies
# df['Names'] = Names
# df['emails'] = emails

writer = ExcelWriter(path)
df.to_excel(writer, 'Sheet1')
writer.save()