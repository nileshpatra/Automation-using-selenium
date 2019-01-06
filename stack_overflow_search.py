import selenium
from selenium import webdriver
from selenium.webdriver.common import keys

message = 'python key not found'
driver = webdriver.Firefox()
driver.get('https://stackoverflow.com/')
driver.find_element_by_xpath('/html/body/header/div/form/div/input').send_keys(message)
driver.find_element_by_xpath('/html/body/header/div/form/div/input').send_keys(u'\ue007')

