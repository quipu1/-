# 아이템 기반 추천
# 협업 필터링
### 이 부분은 백엔드 로직에 녹여야할듯
import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

import warnings

warnings.filterwarnings('ignore')


### 맥주간 유사도 기반 추천
data = pd.read_csv('전처리후데이터.csv', encoding='utf-8', index_col=0)

ratings = data.copy()

# 피벗 테이블을 이용해 유저-아이디 매트릭스 구성
ratings_matrix = ratings.pivot_table('평점', index='아이디', columns='맥주')
ratings_matrix.head(3)
# fillna함수를 이용해 Nan처리
ratings_matrix = ratings_matrix.fillna(0)
# print(ratings_matrix)

# 유사도 계산을 위해 트랜스포즈
ratings_matrix_T = ratings_matrix.transpose()
# print(ratings_matrix_T)

# 아이템-유저 매트릭스로부터 코사인 유사도 구하기
item_sim = cosine_similarity(ratings_matrix_T, ratings_matrix_T)

# cosine_similarity()로 반환된 넘파이 행렬에 영화명을 매핑해 DataFrame으로 변환
item_sim_df = pd.DataFrame(data=item_sim, index=ratings_matrix.columns, columns=ratings_matrix.columns)

# print(item_sim_df.shape)
# print(item_sim_df.head(3))

ratings_matrix.columns

# 호가든 맥주와 유사도가 높은 맥주 5개만 추출하기
print(item_sim_df['Hoegaarden'].sort_values(ascending=False)[:5])