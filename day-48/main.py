from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\development\chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://www.python.org/")
time = driver.find_elements(By.CSS_SELECTOR, ".blog-widget li time")
body = driver.find_elements(By.CSS_SELECTOR, ".blog-widget li a")
for i in body:
    print(i.text)
d = {time[n].text: body[n].text for n in range(5)}
print(d)