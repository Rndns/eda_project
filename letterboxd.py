import requests as req
from bs4 import BeautifulSoup
import pandas as pd
import csv

# 받아오는 형식에 따라 for문 사용
movie_names = []

f = open('./csvFile/title_name.csv', 'r')

df_name = csv.reader(f)

for i in df_name:
    i[2].strip().replace('  ', ' ')
    movie_names.append(i[2].lower().replace(' ','-'))

review_name_list = []
review_grade_list = []
review_text_list = []

dict_star = {'½':0.5, '★':1.0, '★½':1.5 ,'★★':2.0 ,'★★½':2.5 ,'★★★':3.0 ,'★★★½':3.5 ,'★★★★':4.0 ,'★★★★½':4.5 ,'★★★★★':5.0}

# 영화 이름 리스트 돌면서 1~8 페이지 순환 
for name in movie_names:

    for page_num in range(1,9):

        url = 'https://letterboxd.com/film/{}/reviews/by/added/page/{}/'.format(name, page_num)

        res = req.get(url).text

        root = BeautifulSoup(res, 'html.parser')

        # review list
        review_list = root.find_all('li', {'class':'film-detail'})
        
        # grade 클래스 이름에서 수치 가지고 오기
        if not review_list:
            print(1, name)
            break

        for review_num in review_list:

            review_star = None
            review_text = None

            if review_num.find('span', class_ = 'rating'):
                review_star = review_num.find('span', class_ = 'rating').text
                review_star = dict_star[review_star.strip()]

            # 코멘트
            if review_num.find('div', class_ = 'body-text'):
                review_text = review_num.find('div', class_ = 'body-text').text

            review_name_list.append(name)
            review_grade_list.append(review_star)
            review_text_list.append(review_text)

letterboxd_review = pd.DataFrame(zip(review_name_list, review_grade_list, review_text_list), columns=['name', 'star', 'text'])

letterboxd_review.to_csv('./csvFile/letterboxd.csv')

print(letterboxd_review)