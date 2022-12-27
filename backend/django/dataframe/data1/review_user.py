import pandas as pd
import numpy as np
### 맥주 리뷰 데이터

review_data = pd.read_csv('data/전체리뷰리스트.csv', encoding='utf-8', index_col=0)

# beers = pd.DataFrame(review_data['beer_eng_name']).groupby(['beer_eng_name']).size().reset_index()

# print(beers)
# beers.to_csv('beers1.csv', encoding='utf-8')


beer_data = pd.read_csv('data/beers.csv', index_col=0)

beer_data.index = beer_data.index + 1

beer_data = beer_data['beer_eng_name'].reset_index().rename(columns={'index':'beer_id'})
beer_data.to_csv('beerlist.csv', encoding='utf-8')
review_data = review_data[['user_id', 'beer_eng_name', 'review_score']].rename(columns={'review_score':'score'})

# print(beer_data)
# print(review_data)

reviews = pd.merge(review_data, beer_data, on='beer_eng_name', how='left')
reviews = reviews[['user_id', 'score', 'beer_id']]
reviews['beer_id'] = reviews['beer_id'].astype(np.int64)


print(reviews)
# print(reviews['beer_id'].astype(str).str.split('.').str[0].fillna(''))

# 여기서 csv로 하나 만들기
# reviews.to_csv('reviews.csv', encoding='utf-8')

# users = pd.DataFrame(reviews['user_id']).groupby(['user_id']).size()
# users_data = pd.DataFrame(users).reset_index()
# users_data = pd.DataFrame(users_data['user_id'])

# print(users_data)
# users_data.to_csv('users.csv', encoding='utf-8')


