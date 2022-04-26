import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://twitter.com'
email = os.environ["GMAIL"]
twitter_pass = os.environ["TWITTER_PASS"]
# print(password)
service = Service("C:\development\chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(URL)

time.sleep(1)
log = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
log.click()
time.sleep(3)
log_mail = driver.find_element(By.NAME, 'text')
log_mail.send_keys("AnonEstkis")
log_mail.send_keys(Keys.ENTER)
time.sleep(3)
log_pass = driver.find_element(By.NAME, 'password')
log_pass.send_keys(twitter_pass)
log_pass.send_keys(Keys.ENTER)
time.sleep(5)
area = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
area.send_keys("hiiii")
btn = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
btn.click()
