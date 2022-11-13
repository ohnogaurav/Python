#Auto filling websites and forms

from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://sbi.com')

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('Saurav2004')

passwordElem = browser.find_element_by_id('login-password')
passwordElem.send_keys('saurav@2004')

passwordElem.submit()
