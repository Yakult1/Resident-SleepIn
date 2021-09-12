from selenium import webdriver
from selenium.webdriver.common.by import By
import time

### INSERT INSTALLATION DIRECTORY IN THE QUOTATIONS ###
driver = webdriver.Chrome(" ")

### INSERT FORM URL IN THE QUOTATIONS
url = (" ")

time.sleep(1)

driver.get(url)

### INSERT SCHOOL EMAIL IN THE QUOTATIONS ###
email = " "
first_email = driver.find_element_by_xpath('//[@id="identifierId"]')
first_email.send_keys(email)

nextButton = driver.find_element_by_xpath('//[@id="identifierNext"]/div/button')
nextButton.click()

time.sleep(6)

### INSERT CEDP USERNAME IN THE QUOTATIONS ###
ce_username = " "
cedp_username = driver.find_element_by_xpath('//[@id="Ecom_User_ID"]')
cedp_username.send_keys(ce_username)

### INSERT CEDP PASSWORD IN THE QUOTATIONS ###
ce_password = " "
cedp_password = driver.find_element_by_xpath('//[@id="Ecom_Password"]')
cedp_password.send_keys(ce_password)

LogInButton = driver.find_element_by_xpath('//[@id="submitField"]')
LogInButton.click()

time.sleep(10)

continueButton = driver.find_element_by_xpath('//[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
continueButton.click()

time.sleep(4)

nextButton2 = driver.find_element_by_xpath('//[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
nextButton2.click()

time.sleep(1)

nextButton3 = driver.find_element_by_xpath('//[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
nextButton3.click()

time.sleep(1)

submitButton = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
submitButton.click()