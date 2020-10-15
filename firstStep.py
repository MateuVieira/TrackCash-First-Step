import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Url to login 
URL = 'https://marketplace.integracommerce.com.br/Account/Login'

# Test credentials - provided by TrackCash
#credenciais1
LOGIN='desenvolvimento@comprenet.com.br'
PASSWORD='tecnol@gia2@17'

# Set selenium options
options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get(URL)

# Delay of 10 sec to load page
time.sleep(10)

fieldLogin = driver.find_element_by_xpath('//*[@id="username"]')
fieldLogin.send_keys(LOGIN)

fieldPassword = driver.find_element_by_xpath('//*[@id="password"]')
fieldPassword.send_keys(PASSWORD)

# End browser
# driver.quit()
