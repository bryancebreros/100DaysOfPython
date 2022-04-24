import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://www.linkedin.com/jobs/search/?f_WT=2&geoId=103323778&keywords=web%20developer&location=Mexico'
password = os.environ["LINKEDIN"]
PHONE = os.environ["PHONE_NUMBER"]
# print(password)
service = Service("C:\development\chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(URL)
sign = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign.click()
email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys("cebrerosbryan@gmail.com")
passw = driver.find_element(By.XPATH, '//*[@id="password"]')
passw.send_keys(password)
passw.send_keys(Keys.ENTER)
time.sleep(5)
apply_button = driver.find_element(By.XPATH, '//*[@id="ember183"]')
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
#Submit the application
save = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/button/span[1]')
save.click()


