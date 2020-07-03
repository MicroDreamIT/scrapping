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

print(forms[9])

browser.close()
