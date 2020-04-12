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
import requests
import uuid 
import random

class api_test_2(unittest.TestCase):

    def setUp(self): 
        logger.info("Initiated api_test_2..")
        
    def test_api_2(self):
        logger.info("Executing test_api_2..")
        try:
            #Load data from data file
            #Load output templates to app level var
            with open('test_data/api_test_data_2.json', 'r') as t:
                logger.info("Reading test data..")
                self.test_data = json.load(t)
                t.close()
            api_url = appLevel.appConfig['API']['URL']
            data = self.test_data
            fName = data["Provider"]["ProviderDemographics"]["FirstName"] + " " + str(uuid.uuid4())
            data["Provider"]["ProviderDemographics"]["FirstName"] = fName[:20]
            lName = data["Provider"]["ProviderDemographics"]["LastName"] + " " + str(uuid.uuid4())
            data["Provider"]["ProviderDemographics"]["LastName"] = lName[:20]

            data["Provider"]["ProviderDemographics"]["IsDummyNPI"] = "True"

            if data["Provider"]["ProviderDemographics"]["IsDummyNPI"] == "True":
                str_npi = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
                data["Provider"]["ProviderDemographics"]["NPI"] = str_npi
            elif data["Provider"]["ProviderDemographics"]["IsDummyNPI"] == "False":
                str_npi = str(random.randint(1,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
                data["Provider"]["ProviderDemographics"]["NPI"] = str_npi
             
            response = requests.post(api_url, json=data)
            #Recieve response
            response_content = 'API response status: ' + str(response.status_code) + '|| reason: ' + str(response.reason) + ' || json: ' + str(response.json) + ' || content: ' + str(response.content)
            logger.info("response: " + response_content)
            self.assertIn("200", str(response.status_code))
            assert "200" in response_content
            logger.info("test_api_2 test executed!!")

        except Exception as e:
            #raise Exception("Exception check!")
            logger.exception(e)

    def test_api_3(self):
        logger.info("Executing test_api_3..")
        try:
            #Load data from data file
            #Load output templates to app level var
            with open('test_data/api_test_data_3.json', 'r') as t:
                logger.info("Reading test data..")
                self.test_data = json.load(t)
                t.close()
            api_url = appLevel.appConfig['API']['URL']
            data = self.test_data
            fName = data["Provider"]["ProviderDemographics"]["FirstName"] + " " + str(uuid.uuid4())
            data["Provider"]["ProviderDemographics"]["FirstName"] = fName[:20]
            lName = data["Provider"]["ProviderDemographics"]["LastName"] + " " + str(uuid.uuid4())
            data["Provider"]["ProviderDemographics"]["LastName"] = lName[:20]

            data["Provider"]["ProviderDemographics"]["IsDummyNPI"] = "True"

            if data["Provider"]["ProviderDemographics"]["IsDummyNPI"] == "True":
                str_npi = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
                data["Provider"]["ProviderDemographics"]["NPI"] = str_npi
            elif data["Provider"]["ProviderDemographics"]["IsDummyNPI"] == "False":
                str_npi = str(random.randint(1,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
                data["Provider"]["ProviderDemographics"]["NPI"] = str_npi
             
            response = requests.post(api_url, json=data)
            #Recieve response
            response_content = 'API response status: ' + str(response.status_code) + '|| reason: ' + str(response.reason) + ' || json: ' + str(response.json) + ' || content: ' + str(response.content)
            logger.info("response: " + response_content)
            self.assertIn("200", str(response.status_code))
            assert "200" in response_content
            logger.info("test_api_3 test executed!!")

        except Exception as e:
            #raise Exception("Exception check!")
            logger.exception(e)

    def tearDown(self):
        logger.info("api_test_2 test completed!!")

if __name__ == "__main__":
    unittest.main()


