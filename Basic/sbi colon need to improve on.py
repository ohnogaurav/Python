#Auto filling websites and forms

from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://sbi.com')

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('username here')

passwordElem = browser.find_element_by_id('login-password')
passwordElem.send_keys('password here')

passwordElem.submit()
