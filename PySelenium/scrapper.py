from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import re
import os
import urllib.request

base_url = "https://programmingwithgilbert.firebaseapp.com/"
videos_url = "https://programmingwithgilbert.firebaseapp.com/videos/keras-tutorials"


#Trying to load the data using urllib. This won't get any data because it can't load data which is loaded after the document.onload function
page = urllib.request.urlopen(videos_url)
soup = BeautifulSoup(page, 'html.parser')
# webdriver path set 
driver = webdriver.Chrome("chromedriver79_win32\chromedriver.exe")
driver.get(videos_url)
driver.implicitly_wait(100)

#To navigate to the specifc pages we nned to get the buttons which a a text of "Watch" and then navigate to each side, scrape the data, save it and go back to the main page
num_links = len(driver.find_elements_by_link_text('Watch'))
code_blocks = []
for i in range(num_links):
    # navigate to link
    button = driver.find_elements_by_class_name("btn-primary")[i]
    button.click()
    # get soup
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('iframe_container'))
    tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')
    tutorial_code_soup = tutorial_soup.find_all('div', attrs={'class': 'code-toolbar'})
    tutorial_code = [i.getText() for i in tutorial_code_soup]
    code_blocks.append(tutorial_code)
    # go back to initial page
    driver.execute_script("window.history.go(-1)")

# After scraping all the needed data we can close the browser session and save the results into .txt files
for i, tutorial_code in enumerate(code_blocks):
    with open('code_blocks{}.txt'.format(i), 'w') as f:
        for code_block in tutorial_code:
            f.write(code_block+"\n")