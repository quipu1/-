### 맥주 리스트 만들기

from beer_eng_list import beer_eng_list
import json
import pandas as pd
import os
import shutil
import simplejson
import numpy as np
from pandas.core.frame import DataFrame


DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "beers.json")


# beers_columns = {
#     "beer_kor_name",
#     "beer_eng_name",
#     "class",
#     "country",
#     "description"
# }

try:
    with open(DATA_FILE, 'rt', encoding="utf-8") as f:
        data = json.loads(f.read())
except FileNotFoundError as e:
    print(f"`{DATA_FILE}` 가 존재하지 않습니다.")
    exit(1)

beers = []

for d in data:
    
    beers.append(
        [
            d["beer_kor_name"],
            d["beer_eng_name"],
            d["class"],
            d["country"],
            d["description"]
        ]
    )

beers_frame = pd.DataFrame(data=beers, columns=list(data[0].keys()))
# beers_frame = beers_frame.reindex(columns=list(data[0].keys()))
# print(beers_frame)

# beers_frame.to_csv('전체맥주리스트2.csv', encoding='utf-8')


# print(beers_frame)

score_data = pd.read_csv('전체맥주리뷰평균점수.csv', encoding='utf-8', index_col=0)

beers_data = pd.merge(beers_frame, score_data, on='beer_kor_name', how='left')

beers_data.rename(columns={'beer_eng_name_x':'beer_eng_name'}, inplace=True)
beers_data.drop(['beer_eng_name_y'], axis=1, inplace=True)

beers_data.to_csv('전체맥주리스트3.csv', encoding='utf-8')
# print(beers_data)