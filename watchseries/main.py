from os import getcwd
from bs4 import BeautifulSoup
from requests import get, head
from shutil import copyfileobj
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1024x768")
chrome_options.add_extension('/home/lunu/Apps/ublock/ublock.crx')
chrome_options.add_extension('/home/lunu/Apps/uget/uget.crx')
chrome_driver = '/home/lunu/Apps/chromedriver/chromedriver'

browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

browser.get("https://www1.swatchseries.to/dont_trust_the_b----_in_apartment_23/season-2")

episodes = browser.find_elements_by_css_selector('.show-listings li a')
temp = []
for episode in episodes:
  temp.append(episode.get_attribute('href'))
episodes = temp

#No of episodes:
nomb = 19

episodes = episodes[-nomb:]
episodes.reverse()

#starting episode modifier
episodes = episodes[4:]

for episode in episodes:
  browser.get(episode)
  browser.execute_script('showAllLinks();')
  linkList = browser.find_elements_by_css_selector('#myTable tr')
  openloads = []
  for link in linkList:
    tds = link.find_elements_by_css_selector('td')
    linkOk = 0
    linkDomain = tds[0].find_element_by_css_selector('span').get_attribute('innerText')
    if 'openload' not in linkDomain:
      continue
    theLink = tds[1].find_element_by_css_selector('a').get_attribute('href')
    openloads.append(theLink)
  if len(openloads) != 4:
    print('failed on episode \n' + browser.current_url)
    continue
  browser.get(openloads[2])
  openloadLink = browser.find_element_by_css_selector('.fullwrap a').get_attribute('href')

  link = openloadLink
  page_source_len = 0
  while page_source_len < 10000:
    browser.get(link)
    page_source_len = len(browser.page_source)
  browser.find_element_by_css_selector('#btnDl').click()
  sleep(0.3)
  browser.find_element_by_css_selector('.dlbutton').click()
  sleep(0.3)
  ok_link = browser.find_element_by_css_selector('#realdl a').get_attribute('href')
  okdict = head(ok_link, allow_redirects=False).headers
  while 'Location' not in okdict:
    okdict = head(ok_link, allow_redirects=False).headers
  print(okdict['Location'])

browser.close()

