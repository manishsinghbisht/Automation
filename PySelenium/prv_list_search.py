import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time 
import logging
import logzero
from logzero import logger
import json
import appLevel

class prv_list_search(unittest.TestCase):

    def setUp(self):
        logger.info("Initiated prv_list_search..")
        #self.driver = webdriver.Firefox()
        # webdriver path set 
        self.driver = webdriver.Chrome("chromedriver79_win32\chromedriver.exe")
        # To maximize the browser window 
        self.driver.maximize_window() 
        #Load data from data file
        with open('test_data/prv_list_search.json', 'r') as t:
            self.test_data = json.load(t)
            t.close()



    def test_login(self):
        logger.info("Executing test_login..")
        driver = self.driver
        test_data = self.test_data
        try:
            #  link set 
            driver.get(appLevel.appConfig['WEB']['URL']) 
            # Wait for page load
            time.sleep(3) 
            self.assertIn("Sign In", driver.title)

            elem_input_username = driver.find_element_by_id('Email')
            elem_input_username.clear()
            elem_input_username.send_keys(appLevel.appConfig['WEB']['Username']) 

            elem_input_password = driver.find_element_by_id('Password')
            elem_input_password.clear()
            elem_input_password.send_keys(appLevel.appConfig['WEB']['Password']) 

            driver.find_element_by_id('btnSave').click() 
            time.sleep(5)
            
            element1 = WebDriverWait(driver, 10).until(EC.title_contains('Home'))
            element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "leftNav_ParentMenu_Provider")))
            assert "Home" in driver.title

            logger.info("Login test executed!!")

        except Exception as e:
            #raise Exception("Exception check!")
            logger.exception(e)


    def test_prv_list_search(self):
        logger.info("Executing test_prv_list_search..")
        driver = self.driver
        test_data = self.test_data
        try:
            #  link set 
            driver.get(appLevel.appConfig['WEB']['URL']) 
            # Wait for page load
            time.sleep(3) 
            self.assertIn("Sign In", driver.title)

            elem_input_username = driver.find_element_by_id('Email')
            elem_input_username.clear()
            elem_input_username.send_keys(appLevel.appConfig['WEB']['Username']) 

            elem_input_password = driver.find_element_by_id('Password')
            elem_input_password.clear()
            elem_input_password.send_keys(appLevel.appConfig['WEB']['Password']) 

            driver.find_element_by_id('btnSave').click() 
            time.sleep(5)
            
            element1 = WebDriverWait(driver, 10).until(EC.title_contains("Home"))
            element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "leftNav_ParentMenu_Provider")))
            assert "Home" in driver.title

            # Provider List
            driver.find_element_by_id('leftNav_ParentMenu_Provider').click() 
            driver.find_element_by_id('leftNav_ProviderList_Link').click() 
            time.sleep(5) 

            #Search
            elem_input_searchFirstName = driver.find_element_by_id(test_data["page_providerlist"]["elem_firstname_id"])
            elem_input_searchFirstName.clear()
            elem_input_searchFirstName.send_keys(test_data["page_providerlist"]["elem_firstname_id_data"])

            elem_input_searchFirstName = driver.find_element_by_id(test_data["page_providerlist"]["elem_lastname_id"])
            elem_input_searchFirstName.clear()
            elem_input_searchFirstName.send_keys(test_data["page_providerlist"]["elem_lastname_id_data"])
            elem_input_searchFirstName.send_keys(Keys.RETURN)

            time.sleep(5) 

            assert "No results found." not in driver.page_source

            logger.info('Provider List and search test executed!') 

            #elem = driver.find_element_by_name("q")
            #elem.send_keys("pycon")
            #elem.send_keys(Keys.RETURN)
            #assert "No results found." not in driver.page_source
        except Exception as e:
            #raise Exception("Exception check!")
            logger.exception(e)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


