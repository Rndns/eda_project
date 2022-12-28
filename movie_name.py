from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as req
import re
import pandas as pd

path = '/opt/homebrew/bin/chromedriver'

driver = webdriver.Chrome(path)


# login
time.sleep(15)
s = req.Session()
headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
}
s.headers.update(headers)

for cookie in driver.get_cookies():
    c = {cookie['name'] : cookie['value']}
    s.cookies.update(c)


kor_titles = {
        '드라마' : [],
         '판타지'  : [],
         '공포' : [],
         '멜로/애정/로맨스' : [],
         '모험' : [],
         '스릴러' : [],
         '느와르' : [],
         '다큐멘터리' : [],
         '코미디' : [],
         '가족' : [],
         '미스터리' : [],
         '전쟁' : [],
         '애니메이션' : [],
         '범죄' : [],
         '뮤지컬' : [],
         'SF' : [],
         '액션' : [],
         }

genre = ['드라마',
         '판타지',
         '공포',
         '멜로/애정/로맨스',
         '모험',
         '스릴러',
         '느와르',
         '다큐멘터리',
         '코미디',
         '가족',
         '미스터리',
         '전쟁',
         '애니메이션',
         '범죄',
         '뮤지컬',
         'SF',
         '액션']

P_num = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# kor name dict
for X, page in enumerate(P_num):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20221220&tg={}'.format(page)
    resp = req.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    a_tags = soup.select('tbody a')
    a_tag2 = a_tags[0::2]
    for tag in a_tag2:
        kor_titles[genre[X]].append(tag.text.strip())

eng_titles = {
        '드라마' : [],
         '판타지'  : [],
         '공포' : [],
         '멜로/애정/로맨스' : [],
         '모험' : [],
         '스릴러' : [],
         '느와르' : [],
         '다큐멘터리' : [],
         '코미디' : [],
         '가족' : [],
         '미스터리' : [],
         '전쟁' : [],
         '애니메이션' : [],
         '범죄' : [],
         '뮤지컬' : [],
         'SF' : [],
         '액션' : [],
         }

kor_name = []
eng_name = []
genre_name = [] 

# eng name dict
for X, page in enumerate(P_num):
    
    driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20221220&tg={}'.format(page))
    
    for name in kor_titles[genre[X]]:
        kor_name.append(name)
        genre_name.append(genre[X])

        driver.find_element(By.XPATH, "//a[@title='{}']".format(name)).click()
        
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        eng_title_text = soup.select('strong.h_movie2')

        eng_list = eng_title_text[0]['title'].split(',')
        eng_list_clean = []

        # alpha, space 만 살리기
        for eng in eng_list:
            eng_clean = re.sub('[^a-zA-Z\s]', '', eng.strip())

            if re.sub('[^a-zA-Z]', '', eng_clean).isalpha():
                eng_list_clean.append(eng_clean.strip())
        
        if not len(eng_list_clean):
            eng_name.append(None)
        
        elif eng_list_clean[0] in ['I', 'II', 'III']:
            eng_name.append(eng_list_clean[1])

        else:
            eng_name.append(eng_list_clean[0])

        driver.back()
        # time.sleep(1)

# make csv
df_titles = pd.DataFrame(zip(kor_name, eng_name, genre_name), columns=['name', 'eng name', 'genre'])

print(df_titles)

df_titles.to_csv("./csvFile/title_name.csv")