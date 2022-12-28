from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = '/opt/homebrew/bin/chromedriver'

driver = webdriver.Chrome(path)

m_list=['스파이더맨','아이언맨']
related = []
count = 0
for i in m_list:

    url1='https://pedia.watcha.com/ko-KR/search?query={}&category=contents'.format(i)
    driver.get(url1)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,'css-8y23cj').click()
    time.sleep(2)
    url2=driver.current_url+'/comments'
    driver.get(url2)

    #prev_height =driver.execute_script("window.scrollTo(0,2)")
    prev_height = driver.execute_script("return document.body.scrollHeight")
    print(1)
    while True:
        #현재높이 저장
        current_height = driver.execute_script("return document.body.scrollHeight")
        
        #첫번째로 스크롤 내리기
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        #시간대기
        time.sleep(1.2)
        count+=1

        print(f"{count}:{current_height}")

        #현재높이와 끝의 높이가 끝이면 탈출
        #if (count==9)|(count==19):
            #break
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == current_height:
            break

        #업데이트해줘서 끝낼 수 있도록
        current_height = new_height

    div_tags=driver.find_elements(By.CLASS_NAME,'css-1g78l7j')

    for i in div_tags:
        print(i.text)
    
    #time.sleep(2)
    #soup = BeautifulSoup(div_tags, 'html.parser')
    #print(soup)
    #div_tags =  soup.find_all('div', {'class':'css-1g78l7j'})
        
    #for div_tag in div_tags:
        #related.append(div_tag.text)
    #print(related)