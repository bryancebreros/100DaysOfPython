import os

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://www.instagram.com/'
user = 'rayansitos'
ig_pass = os.environ["IG_PASS"]
# print(password)
service = Service("C:\development\chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(URL)

time.sleep(2)
log = driver.find_element(By.NAME, 'username')
log.send_keys(user)
password = driver.find_element(By.NAME, 'password')
password.send_keys(ig_pass)
password.send_keys(Keys.ENTER)
time.sleep(3)
driver.get(URL +'aliceoverall/')
following = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
following.click()
time.sleep(4)
modal = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]')
for i in range(10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    time.sleep(2)
all_buttons = driver.find_elements(By.CSS_SELECTOR, "li button")
for button in all_buttons:
    try:
        button.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
        cancel_button.click()


