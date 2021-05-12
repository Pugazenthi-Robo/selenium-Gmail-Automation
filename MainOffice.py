from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support.select import Select
#os.startfile('chromedriver.exe')
import win32com.client
browser = webdriver.Chrome()


#Time in hours
totaltime = 8
#gmail 
gmail=""
#gmail password
password=""



def ti(x):
    browser.get('https://www.google.com/intl/en-GB/gmail/about/#')
    browser.find_element_by_link_text("Sign in").click()
    browser.switch_to.window(browser.window_handles[-1])
    emailElem = browser.find_element_by_id('identifierId')
    emailElem.send_keys(gmail + Keys.RETURN)
    browser.implicitly_wait(5)
    passwordElem = browser.find_element_by_name('password')
    passwordElem.send_keys(password + Keys.RETURN)
    time.sleep(30)
    browser.refresh()
    time.sleep(15)
    #refresh interval of 15 min
    for i in range(x):
        print("refresh")
        browser.refresh()
        time.sleep(900)
        print("refresh")
        browser.refresh()
        time.sleep(900)
        print("refresh")
        browser.refresh()
        time.sleep(900)
        print("refresh")
        browser.refresh()
        time.sleep(900)

ti(totaltime)

browser.quit()
#os.system("TASKKILL /F /IM chromedriver.exe")

