from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

path = '/opt/homebrew/bin/chromedriver'

driver = webdriver.Chrome(path)

time.sleep(1)

url = 'https://pedia.watcha.com/ko-KR'

driver.get(url)

time.sleep(2)

driver.find_element(By.XPATH, "//label[@class='css-kyr608']").click()

time.sleep(2)

driver.find_element(By.XPATH, "//label[@class='css-kyr608']").send_keys('Green Book')

time.sleep(2)

driver.find_element(By.XPATH, "//label[@class='css-kyr608']").send_keys(Keys.ENTER)

time.sleep(2)

driver.find_element(By.XPATH, "//a[@title='그린 북']").click()

time.sleep(2)