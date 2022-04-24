from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:\development\chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Hyunjin")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Guapa")
email = driver.find_element(By.NAME, "email")
email.send_keys("hyunjinsita@loona.com")
email.send_keys(Keys.ENTER)


# articles = driver.find_element(By.NAME, "search")
# articles.send_keys("Loona")
# articles.send_keys(Keys.ENTER)
# loona = driver.find_element(By.CLASS_NAME, "searchmatch")
# loona.click()
# chuu = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[2]/td/div/a')
# chuu.click()
