import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Url to login 
URL = 'https://marketplace.integracommerce.com.br/Account/Login'

# Set selenium options
options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get(URL)

# End browser
# driver.quit()
