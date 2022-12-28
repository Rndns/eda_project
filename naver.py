from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = '/opt/homebrew/bin/chromedriver'

driver = webdriver.Chrome(path)

time.sleep(1)

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20221220&tg=1'

driver.get(url)

time.sleep(2)

driver.find_element(By.XPATH, "//a[@title='가버나움']").click()

time.sleep(2)



