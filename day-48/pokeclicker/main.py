from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

game = True
service = Service("C:\development\chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://www.pokeclicker.com/")


select = driver.find_element(By.XPATH, '//*[@id="saveSelector"]/div[1]/div[4]/label[1]')
select.click()
driver.implicitly_wait(40)
select2 = driver.find_element(By.XPATH, '//*[@id="startSequenceModal"]/div/div/div[3]/button[2]')

select2.click()
squirtle = driver.find_element(By.XPATH, '//*[@id="starterSelection"]/div[3]/input')
squirtle.click()

screen = driver.find_element(By.XPATH, '//*[@id="battleContainer"]/div[2]/div[1]/div')
btn = driver.find_element(By.XPATH, '//*[@id="starterCaughtModal"]/div/div/div[3]/button')
btn2 = driver.find_element(By.XPATH, '/html/body/div[51]/div/div[5]/a')

while game:
    screen.click()
    if btn:
        btn.click()
    if btn2:
        btn2.click()