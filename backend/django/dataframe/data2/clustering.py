import pandas as pd

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as po

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler

import warnings

warnings.filterwarnings('ignore')
pd.set_option('display.max_rows', 100)

data = pd.read_csv('전처리후데이터.csv', encoding='utf-8', index_col=0)
# print(data.head(3))

### 맥주별 평점 계산
tmp = data.copy()
tmp = tmp[['맥주']]

# 맥주 이름 중복행 제거 : df.drop_duplicates()
tmp.drop_duplicates(keep='first', inplace=True)
cols = ['Aroma','Appearance','Flavor','Mouthfeel','Overall']

# 5가지 요소를 컬럼에 추가합니다.
for col in cols:
    tmp[col] = ''
# print(tmp.head(5))

# 전체 맥주 개수만큼 실행
for i in range(len(tmp)):
    # 맥주 이름 추출
    beer = tmp['맥주'].iloc[i]

    # 평가한 유저 수
    length = len(data[data['맥주']==beer])
    # 5가지 평가 요소 계산
    for col in cols:
        # 요소별 평점 합
        col_sum = data[data['맥주']==beer][col].sum()
        # 요소별 평균 구하기
        tmp[col].iloc[i] = col_sum/length

tmp.to_csv('맥주_종류별_평점.csv', encoding='utf-8')
# print(tmp.head(5))


### 클러스터링
beer_names = data[['맥주']]

beer_values = data[['Aroma','Appearance','Flavor','Mouthfeel','Overall']]

# 값 표준화
scaler = MinMaxScaler()

scaler.fit(beer_values)

scaled = scaler.transform(beer_values)
# print(scaled)


def elbow(X):
    sse = []

    for i in range(1,11):
        km = KMeans(n_clusters=i)
        km.fit(X)
        sse.append(km.inertia_)

    fig = px.line(sse)
    fig.show()

elbow(scaled)

km = KMeans(n_clusters=3).fit(scaled)
km.cluster_centers_

# 클러스터링을 통해 맥주별 군집 예측
predict = pd.DataFrame(km.predict(scaled))
predict.columns = ['Cluster']
# print(predict.head(3))

scaled = pd.DataFrame(data=scaled, columns=['Aroma', 'Appearance', 'Flavor', 'Mouthfeel','Overall'])
# print(scaled)

# 이거 맞춰줘야함
beer_names.reset_index(inplace=True, drop=True)

# scale 값과 클러스터링 예측값, 기존 맥주이름, 편의점 데이터 병합
result = pd.concat([scaled, beer_names], axis=1).reset_index(drop=True)

# scale 값과 클러스터링 예측값, 기존 맥주이름, 편의점 데이터 병합
result = pd.concat([result, predict], axis=1).reset_index(drop=True)
# print(result)

c_result = km.cluster_centers_
c_result = pd.DataFrame(data=c_result)
c_result.columns = ['Aroma', 'Appearance', 'Flavor','Mouthfeel','Overall']
c_result.sort_values(by='Overall', inplace=True)
print(c_result)

# c_result.to_csv('대표군집클러스터링.csv', encoding='utf-8')
# result.to_csv('전체맥주클러스터링.csv', encoding='utf-8')