from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
browser.get("https://www.google.com")
# browser.get("file:///Users/shahanurmdsharif/development/python/scrapping/scrap.html")
