from bs4 import BeautifulSoup
from selenium import webdriver
import time


class LoadWebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    show_browser = 0
    if show_browser:
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Chrome(options=options)
