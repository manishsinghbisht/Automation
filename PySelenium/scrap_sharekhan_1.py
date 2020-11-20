from bs4 import BeautifulSoup	
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import re
import os
import urllib.request
import time 

base_url = "https://trade.sharekhan.com"


##Trying to load the data using urllib. This won't get any data because it can't load data which is loaded after the document.onload function
#page = urllib.request.urlopen(videos_url)
#soup = BeautifulSoup(page, 'html.parser')
# webdriver path set 
driver = webdriver.Chrome("chromedriver79_win32\chromedriver.exe")
driver.get(base_url)
driver.maximize_window() 
time.sleep(5) 

username_input = driver.find_element_by_name('emailLoginId')
username_input.send_keys("mans80") 
driver.implicitly_wait(5)
#Enter key for NEXT link
username_input.send_keys(u'\ue007')
driver.implicitly_wait(5)

username_pass = driver.find_element_by_name('br_pwd')
username_pass.send_keys("l@#") 
driver.implicitly_wait(5)
#Enter key for LOGIN link
username_pass.send_keys(u'\ue007')
driver.implicitly_wait(30)


#elem = driver.find_element_by_partial_link_text("View Detailed Portfolio")
# elem = driver.find_elements_by_link_text('View Detailed Portfolio')
elem = driver.find_element_by_xpath("/html/body/div[3]/ui-view/div/div[2]/div[1]/div[2]/span[1]")

elem.click()


driver.implicitly_wait(50)




