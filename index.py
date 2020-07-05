from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
show_browser = 0
if show_browser:
    browser = webdriver.Chrome()
else:
    browser = webdriver.Chrome(options=options)

browser.get("file:///Users/shahanurmdsharif/development/python/scrapping/scrap.html")
time.sleep(2)
html = browser.page_source

source = BeautifulSoup(html, features="html.parser")

forms = source.find_all('form')

table = forms[0].find('tbody')
inputs = table.find_all('input')
for inp in inputs:
    if inp.get('name') == 'firstname':
        firstname = inp.get('value')

    if inp.get('name') == 'lastname':
        lastname = inp.get('value')

    if inp.get('name') == 'gender':
        gender = inp.get('value')

    if inp.get('name') == 'address':
        address = inp.get('value')

    if inp.get('name') == 'zipcode':
        zipcode = inp.get('value')

    if inp.get('name') == 'city':
        city = inp.get('value')

    if inp.get('name') == 'country':
        country = inp.get('value')

    if inp.get('name') == 'phone':
        phone = inp.get('value')


browser.close()
# table.find('input', {"name": "username"})
# username.get('value')
