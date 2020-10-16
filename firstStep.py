import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def loadPageAndSingUp(LOGIN, PASSWORD):
  # Delay of 5 sec to load page
  time.sleep(5)

  # Insert login info
  fieldLogin = driver.find_element_by_xpath('//*[@id="username"]')
  fieldLogin.send_keys(LOGIN)

  # Insert password info
  fieldPassword = driver.find_element_by_xpath('//*[@id="password"]')
  fieldPassword.send_keys(PASSWORD)

  # Click on button to singup on page
  driver.find_element_by_xpath('//*[@id="kc-login"]').click()

def normalizeDateVar(dateVar):
  listOfDateToInt = [int(i) for i in dateVar]
  return listOfDateToInt

def formatDateLongText(day, month, year):
  # Arry with the names of the months in pt-Br
  arrMonths = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

  monthLong = arrMonths[month - 1]

  return f'{day} de {monthLong} de {year}'

def formatDate (start, end):
  # Expected format - dd/MM/YYYY

  # Separating the date information
  dateStart = normalizeDateVar(start.split('/'))
  dateEnd = normalizeDateVar(end.split('/'))

  # Creating an object with the information for the time period request
  dateFormated = {
    'chosedMonth': dateStart[1],
    'chosedYear': dateStart[2],
    'chosedStartDay': formatDateLongText(dateStart[0], dateStart[1], dateStart[2]),
    'chosedEndDay': formatDateLongText(dateEnd[0], dateEnd[1], dateEnd[2]),
  }

  return dateFormated

def resquestDataForPeriodOfTime(URL_DATA, formatedDate):

  time.sleep(2)

  # Searching for the calendar element on the page and opening the calendar
  fieldDate = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[1]')
  fieldDate.click()

  # Searching the button for selecting the year and month
  buttonChoseYearAndMonth = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/button[3]')

  time.sleep(1)

  # Performing two clicks to set the choice of year and month of the start date
  buttonChoseYearAndMonth.click()
  buttonChoseYearAndMonth.click()

  time.sleep(1)

  # Choosing the starting year
  chosedYear = formatedDate['chosedYear']
  buttonChosedYear = driver.find_element_by_xpath(f'//*[@id="root"]/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[2]/div/div/button[text()="{chosedYear}"]')
  buttonChosedYear.click()

  time.sleep(1)

  # Choosing the starting month
  chosedMonth = formatedDate['chosedMonth']
  buttonChosedMonth = driver.find_element_by_xpath(f'//*[@id="root"]/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[2]/div/div/button[{chosedMonth}]')
  buttonChosedMonth.click()

  # Choosing the starting day
  chosedDayStart = formatedDate['chosedStartDay']
  buttonChosedDayStart = driver.find_element_by_xpath(f'//*[@id="root"]/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/button[*]/abbr[@aria-label="{chosedDayStart}"]')
  buttonChosedDayStart.click()

  time.sleep(1)

  # Choosing the ending day
  chosedDayEnd = formatedDate['chosedEndDay']
  buttonChosedDayEnd = driver.find_element_by_xpath(f'//*[@id="root"]/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/button[*]/abbr[@aria-label="{chosedDayEnd}"]')
  buttonChosedDayEnd.click()

# Url to login 
URL = 'https://marketplace.integracommerce.com.br/Account/Login'

# Url to take data
URL_DATA = 'https://cdn.integracommerce.com.br/site/production/index.html#/Order'

# Test credentials - provided by TrackCash
#credenciais1
LOGIN='desenvolvimento@comprenet.com.br'
PASSWORD='tecnol@gia2@17'

# Info to search data for a period of time
START = '01/01/2018'
END = '01/02/2018'

# Set selenium options
options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

# Request page by URL
driver.get(URL)
loadPageAndSingUp(LOGIN, PASSWORD)
time.sleep(2) #Delay to load page
formatedDate = formatDate(START, END)
# Load data page
driver.get(URL_DATA)
resquestDataForPeriodOfTime(URL_DATA, formatedDate)
time.sleep(2) #Delay to load data on page


# # End browser
# driver.quit()

