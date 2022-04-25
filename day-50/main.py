import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://tinder.com/app/recs'
email = os.environ["HOTMAIL"]
fb_pass = os.environ["FB_PASS"]
# print(password)
service = Service("C:\development\chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(URL)

time.sleep(1)
log = driver.find_element(By.XPATH, '//*[@id="q939012387"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log.click()
time.sleep(3)
fb = driver.find_element(By.XPATH, '//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb.click()
time.sleep(7)
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys(email)
pass_input = driver.find_element(By.NAME, 'pass')
pass_input.send_keys(fb_pass)
email_input.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
time.sleep(5)
location = driver.find_element(By.XPATH, '//*[@id="q-789368689"]/div/div/div/div/div[3]/button[1]')
location.click()
notif = driver.find_element(By.XPATH, '//*[@id="q-789368689"]/div/div/div/div/div[3]/button[2]')
notif.click()
# I WAS BLOCKED :(