from os import getcwd
from bs4 import BeautifulSoup
from requests import get
from shutil import copyfileobj
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1024x768")
chrome_options.add_extension('/home/lunu/Apps/ublock/ublock.crx')
chrome_driver = '/home/lunu/Apps/chromedriver/chromedriver'

browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

#setup
browser.get('https://www1.cartooncrazy.tv/anime/bleach/')
sleep(10)
show_name = 'Bleach'
start_from = 0 # from which no. link should download start from
episode_no = 1 # Starting no. of episode.
to_download = 10 # No. of episodes to be downloaded

episodesStale = browser.find_elements_by_css_selector('#episode-list-entry-tbl a')
episodesStale.reverse()
episodes = []
episodesStale = episodesStale[start_from:]
for episode in episodesStale:
  episodes.append(episode.get_attribute('href'))

links = []

Downloaded = 0

fle = open("links.txt", "a")

for episode in episodes:
  link = episode
  browser.get(link)
  if Downloaded == toDownload:
    break
  flag = 1
  while flag == 1:
    try:
      browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[1])
      browser.find_element_by_css_selector('#myvid').click()
      flag = 0
    except:
      print('trying to refresh page')
      browser.refresh()
  episodeLink = browser.find_element_by_css_selector('video').get_attribute('src')
  links.append(episodeLink)
  fle.write(episodeLink + '\n')
  Downloaded += 1
browser.close()

name = episode_no

print('Do you want to download the episodes as well?')
if ('y' or 'Y' in input()):
  #very slow, single connection and 1 episode at a time.
  #better use IDM or UGET from links.txt
  for url in links:
    local_filename = show_name + ' ' + str(name) + '.mp4'
    r = get(url, stream=True)
    with open(local_filename, 'wb') as f:
      copyfileobj(r.raw, f)
    name += 1
else:
  print('ok')
