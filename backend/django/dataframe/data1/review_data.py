### 리뷰 리스트

from beer_eng_list import beer_eng_list
import json
import pandas as pd
import os
import shutil
import simplejson
import numpy as np
from pandas.core.frame import DataFrame

from sqlalchemy import create_engine
import pymysql


db_connection_str = 'mysql+pymysql://root:1234@localhost:3306/beer'
db_connection = create_engine(db_connection_str)
conn = db_connection.connect()

beer_reviews_columns = (
    "user_id",
    "beer_kor_name",
    "beer_eng_name",
    "review_score",
    "review_content",
    "writed_at",
)
user_columns = (
    "user_id"
)
DATA_DIR = "data"
beer_reviews = []
users = []
for beer_name in beer_eng_list:
    BEER_REVIEW_DIR =os.path.join(DATA_DIR, "beer_review")
    BEER_REVIEW_DIR =os.path.join(BEER_REVIEW_DIR, f"{beer_name}_reviews.json")
    with open(BEER_REVIEW_DIR, 'rt', encoding="utf-8") as f:
        data = json.loads(f.read())
    i = 0
    for d in data:
        try:
            beer_reviews.append(
                [
                    d["user_id"],
                    d["beer_kor_name"],
                    d["beer_eng_name"],
                    d["review_score"],
                    d["review_content"],
                    d["writed_at"]
                ]
        
            )
            # if d["user_id"] not in users:
            #     users.append([d["user_id"]])
        except:
            pass
# print(users)
beer_reviews_frame = pd.DataFrame(data=beer_reviews, columns=beer_reviews_columns)
# users_frame = pd.DataFrame(data=users, columns=user_columns)
data = {
    "beer_reviews" : beer_reviews_frame,
    # "users" : users_frame
}
pd.to_pickle(data, "DUMPFILE(REVIEW)")

# beer_reviews_frame.to_csv('전체리뷰리스트.csv', encoding='utf-8')

beer_reviews_frame.to_sql(name='test', con=db_connection, if_exists='append',index=False)  