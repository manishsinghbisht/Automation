import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# To run this test: python test_python_org_search.py

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        # webdriver path set  
        self.driver = webdriver.Chrome("chromedriver79_win32\chromedriver.exe")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
