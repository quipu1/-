import pandas as pd
import re

data = pd.read_csv('전체리뷰리스트.csv', encoding='utf-8', index_col=0)

tmp = data.copy()

tmp_group = tmp.groupby(["beer_kor_name", "beer_eng_name"])
tmps = tmp_group.mean()

# print(tmps)
# tmps.info()

# beer_data = tmps[['Aroma', 'Appearance', 'Flavor', 'Mouthfeel']]
# print(beer_data)

tmps.to_csv('전체맥주리뷰평균점수.csv', encoding='utf-8')

beer_data = tmps[[]]
print(beer_data)
beer_data.to_csv('전체맥주리스트.csv', encoding='utf-8')
