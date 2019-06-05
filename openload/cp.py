##recommended header
from requests import get, head
from shutil import copyfileobj
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
#chrome_options.add_argument("--headless")
chrome_options.add_argument("user-data-dir=/home/lunu/.config/google-chrome/Profile 1")
chrome_options.add_argument("--window-size=1024x768")
#yes i use adblock
chrome_options.add_extension('/home/lunu/Apps/ublock/ublock.crx')
chrome_driver = '/home/lunu/Apps/chromedriver/chromedriver'

with webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver) as browser:
  link = 'http://streamplay.to/62bccbllubbh'
  browser.get(link)
  page_source_len = len(browser.page_source)
  #this loop is because my isp sometimes blocks the domain
  #remove this if yours doesn't
  while page_source_len < 500:
    browser.get(link)
    page_source_len = len(browser.page_source)
  x= input()
