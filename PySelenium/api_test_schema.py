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
from jsonschema import validate
import appLevel
import requests

class api_test_schema(unittest.TestCase):

    def setUp(self): 
        #Load data from data file
        #Load output templates to app level var
        with open('test_data/IExchangeAPIStructureTemplate.json', 'r') as t:
            logger.info("Reading IExchange API Structure Template json..")
            self.test_data = json.load(t)
            t.close()

        # Process to keep only those fields which are defined in template
        with open('test_data/api_data_schema.json', 'r') as f:
            self.schema = json.load(f)
            f.close()
    
   

    def test_api_schema(self):
        test_data = self.test_data
        try:
            #Validate dataTemplate.json with dataTemplate_schema.json
            validate(instance=self.test_data, schema=self.schema)
        except Exception as ex:
            logger.error("Schema Error !! " + str(ex.message))

    


    def tearDown(self):
        logger.info("Schema test completed!!")

if __name__ == "__main__":
    unittest.main()


