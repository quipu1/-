import pandas as pd
import re

data = pd.read_csv('전처리후데이터.csv', encoding='utf-8', index_col=0)

tmp = data.copy()

tmp_group = tmp.groupby(["맥주"])
tmps = tmp_group.mean()

tmps.info()

# beer_data = tmps[['Aroma', 'Appearance', 'Flavor', 'Mouthfeel']]
# print(beer_data)