from bs4 import BeautifulSoup	
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import re
import os
import urllib.request
import time 

base_url = "https://www.google.com/finance/"


##Trying to load the data using urllib. This won't get any data because it can't load data which is loaded after the document.onload function
#page = urllib.request.urlopen(videos_url)
#soup = BeautifulSoup(page, 'html.parser')
# webdriver path set 
driver = webdriver.Chrome("chromedriver79_win32\chromedriver.exe")
driver.get(base_url)
driver.maximize_window() 
time.sleep(5) 

#elem = driver.find_element_by_xpath("//a[@class='SVWlSe']")
elem = driver.find_element_by_partial_link_text("Your Stocks")
elem.click()

driver.implicitly_wait(50)




