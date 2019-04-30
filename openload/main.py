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

browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)


def openload(link):
  browser.get(link)
  page_source_len = len(link)

  #this loop is because my isp sometimes blocks the domain
  #remove this if yours doesn't
  while page_source_len < 10000:
    browser.get(link)
    page_source_len = len(browser.page_source)

  browser.find_element_by_css_selector('#btnDl').click()
  sleep(0.3)
  browser.find_element_by_css_selector('.dlbutton').click()
  sleep(0.3)
  ok_link = browser.find_element_by_css_selector('#realdl a').get_attribute('href')
  print(ok_link)
  okdict = head(ok_link, allow_redirects=False).headers

  #this loop is because my isp sometimes blocks the domain
  #remove this if yours doesn't
  while 'Location' not in okdict:
    ok = head(ok_link, allow_redirects=False).headers

  return okdict['Location']


