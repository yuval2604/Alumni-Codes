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


link = "https://www.linkedin.com/search/results/people/?facetConnectionOf=%5B%22ACoAAC4TfPsBxnaXot84GEWqFQ-0UZDtPZcDwUg%22%5D&facetNetwork=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH"
f = requests.get(link)

# print(f.text)

soup = BeautifulSoup(f.text)  # make soup that is parse-able by bs

buttons = soup.find_all('button')


# class_ = "search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary"
# button_list = soup.find_all('button', attrs={'class': class_})
posX = 1272
posY = 319  # 319
D = 131
# pyautogui.position()
confirn_X = 724
confirn_Y = 307

for i in range(6):
    pyautogui.moveTo(posX, posY, duration=0.5)
    time.sleep(1)
    pyautogui.click(x=posX, y=posY, button='left')
    time.sleep(1)
    pyautogui.moveTo(confirn_X, confirn_Y, duration=0.5)
    time.sleep(1)
    pyautogui.click(x=confirn_X, y=confirn_Y, button='left')
    posY += D

# pyautogui.moveRel(posX, posY+D, duration=0.5)

# pyautogui.moveRel(posX, posY+2*D, duration=0.5)

# pyautogui.moveTo(724, 307, duration=0.5)
