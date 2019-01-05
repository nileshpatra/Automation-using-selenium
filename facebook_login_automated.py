import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

username = #'enter username'
password =  #'enter password'
driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')

driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()


