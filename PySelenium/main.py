import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import argparse
import os
import time 
import datetime
import logging
import logzero
from logzero import logger
import json
import appLevel
from prv_list_search import prv_list_search
from api_test_1 import api_test_1
from api_test_2 import api_test_2
from api_test_schema import api_test_schema


def main(args):
    """ Main entry point of the app """
    #config check
    with open('config.json', 'r') as f:
        appLevel.appConfig = json.load(f)
        f.close()
    appLevel.baseDateTimeStampString = datetime.datetime.now().strftime("%y%m%d_%H_%M_%S")
    appLevel.currentDateTimeStampString = appLevel.baseDateTimeStampString
    appLevel.log_file_name = "../" + appLevel.appConfig['DEFAULT']['DATAFOLDER'] + '/test_logfile_' + appLevel.baseDateTimeStampString + '.log'
    # Setup rotating logfile with 10 rotations, each with a maximum filesize of 3MB:
    logzero.logfile(appLevel.log_file_name, maxBytes=3e6, backupCount=10)
    # Set a minimum log level
    logzero.loglevel(logging.INFO)
    try:
        logger.info("Test process initiated!")
        logger.info(args)
        logger.debug("debug check!")
        logger.info("info check!")
        logger.warning("warn check!")
        logger.error("error check!")
        # webdriver path set 
        #browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
        #"C:\\Users\\HP - PC\\Desktop\\Selenium\\chromedriver79_win32\\chromedriver.exe" 
        #browser = webdriver.Chrome("chromedriver79_win32\chromedriver.exe")

        # signin element clicked 
        #browser.find_element_by_xpath("//a[@id ='signin-link']").click() 
        # time.sleep(2) 
        # Login clicked 
        #browser.find_element_by_xpath("//a[@id ='login-email']").click() 
    
        #inputElement.send_keys(Keys.ENTER)
        #inputElement.submit() 
        runner = unittest.TextTestRunner()
        if(appLevel.appConfig['WEB']['TEST_WEB'] == "TRUE"):
            runner.run(suite())
        if(appLevel.appConfig['API']['TEST_API'] == "TRUE"):
            runner.run(api_suite())

    except Exception as e:
        #raise Exception("Exception check!")
        logger.exception(e)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(prv_list_search('test_login'))
    suite.addTest(prv_list_search('test_prv_list_search'))
    return suite

def api_suite():
    suite = unittest.TestSuite()
    suite.addTest(api_test_1('test_iexchange_cache_init'))
    suite.addTest(api_test_1('test_api'))
    suite.addTest(api_test_2('test_api_2'))
    suite.addTest(api_test_2('test_api_3'))
    suite.addTest(api_test_schema('test_api_schema'))
    return suite

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    ## Required positional argument
    #parser.add_argument("arg", help="Required positional argument")

    ## Optional argument flag which defaults to False
    #parser.add_argument("-f", "--flag", action="store_true", default=False)

    ## Optional argument which requires a parameter (eg. -d test)
    #parser.add_argument("-n", "--name", action="store", dest="name")

    ## Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    #parser.add_argument(
    #    "-v",
    #    "--verbose",
    #    action="count",
    #    default=0,
    #    help="Verbosity (-v, -vv, etc)")

    ## Specify output of "--version"
    #parser.add_argument(
    #    "--version",
    #    action="version",
    #    version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)