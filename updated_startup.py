import pyperclip
import time
import webbrowser
import requests
import pandas as pd

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import urllib
import pyautogui
from bs4 import BeautifulSoup

emails = list()

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

######################################################################################################
# creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

# client = gspread.authorize(creds)

# sheet = client.open("Updated Startups").sheet1  # Open the spreadhseet

# # data = sheet.get_all_records()  # Get a list of all records

# # row = sheet.row_values(3)  # Get a specific row
# urls = sheet.col_values(5)  # Get a specific column
# urls = list(urls)


# print(len(urls))

# #####

# urls = urls[1:3]
#####

######################################################################################################

# for link in urls:

link = "https://finder.startupnationcentral.org/company_page/netafim"
f = requests.get(link)

# print(f.text)

soup = BeautifulSoup(f.text)  # make soup that is parse-able by bs
CEO_link = soup.find(
    'div', class_='team-member-cards-wrapper js-team-member-carousel').find('a', href=True)['href']
# f = requests.get(CEO_link)

######################################################################################################
webbrowser.get('chrome').open_new_tab(CEO_link)  # open in chrome

# webbrowser.open_new_tab(CEO_link) -> safari

pyautogui.moveRel(1527, 79, duration=0.25)
time.sleep(2)

pyautogui.click(x=1527, y=79, button='left')
time.sleep(2)

pyautogui.click(x=1514, y=220, button='left')
time.sleep(3)

pyautogui.click(x=1192, y=319, button='left')

emails.append(pyperclip.paste())

print(emails)


# soup = BeautifulSoup(f.text)
