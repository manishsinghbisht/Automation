from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded. 
import time 
# webdriver path set 
#browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
#"C:\\Users\\HP - PC\\Desktop\\Selenium\\chromedriver79_win32\\chromedriver.exe" 
browser = webdriver.Chrome("chromedriver79_win32\chromedriver.exe")
# To maximize the browser window 
browser.maximize_window() 

#  link set 
browser.get('http://inetwork7qa.myienroll.us/') 

# Wait for page load
time.sleep(3) 

# Enter your user name and password here. 
username = "manish.bisht@mySantech.com"
password = "Santech@123"    

#####################
#inputElement.send_keys(Keys.ENTER)
#inputElement.submit() 
#input.get_attribute('value')
#######################
# signin element clicked 
#browser.find_element_by_xpath("//a[@id ='signin-link']").click() 


# time.sleep(2) 

# Login clicked 
#browser.find_element_by_xpath("//a[@id ='login-email']").click() 

# username send 
#a = browser.find_element_by_xpath("//input[@id ='ld-email']") 
#a.send_keys(username) 
username_input = browser.find_element_by_id('Email')
username_input.send_keys(username) 


# password send 
#b = browser.find_element_by_xpath("//input[@id ='ld-password']") 
#b.send_keys(password) 
username_pass = browser.find_element_by_id('Password')
username_pass.send_keys(password) 

# submit button clicked 
#browser.find_element_by_xpath("//input[@id ='ld-submit-global']").click() 
browser.find_element_by_id('btnSave').click() 

time.sleep(3) 

print('Login Successful') 
browser.close() 

