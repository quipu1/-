import re
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from django.contrib.auth import (
    get_user_model,
)
from beers.models import Beer
from boards.models import Board
from beers.serializers import BeerListSerializer
from users.serializers import UserFriendsSerializer, UserListSerializer

import math
import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
from django_pandas.io import read_frame

# Matrix Factorization 협업필터링
@api_view(['GET'])
def predict(request, nickname):
    # DB에 있는 모든 리뷰 가져오기
    qs = Board.objects.all()
    df = read_frame(qs, fieldnames=['nickname', 'beer_id', 'score']).fillna('')

    # 사용자가 리뷰를 안 썼을때
    a = df[df.nickname == nickname]
    review_cnt = len(a)

    if review_cnt == 0:
        data = {
        'review_cnt': review_cnt,
        }

    else:
        big = pd.read_csv('./recommends/data/reviews.csv', encoding='utf-8', index_col=0)
        big = big.rename(columns={'user_id': 'nickname'})
        beers = pd.read_csv('./recommends/data/beerlist.csv', encoding='utf-8', index_col=0)

        # # 두개 이어붙이기
        reviews = pd.concat([df, big])
        print(reviews)

        # # 사용자 기반 협업 필터링 데이터
        data = reviews.pivot_table('score', index='nickname', columns='beer_id').fillna(0)

        matrix = data.to_numpy()
        data_mean = np.mean(matrix, axis=1)
        matrix_data_mean = matrix - data_mean.reshape(-1, 1)

        matrix_data_mean = pd.DataFrame(matrix_data_mean, columns=data.columns)

        U, sigma, Vt = svds(matrix_data_mean, k=12)
        sigma = np.diag(sigma)

        svd_predict_score = np.dot(np.dot(U, sigma), Vt) + data_mean.reshape(-1, 1)
        df_svd_preds = pd.DataFrame(svd_predict_score, columns=data.columns, index=data.index)

        sort_user_predict = df_svd_preds.loc[nickname].sort_values(ascending=False)
        
        user_data = reviews[reviews.nickname == nickname].sort_values(['score'], ascending=False)
        recommend = beers[~beers['beer_id'].isin(user_data['beer_id'])]
        recommend = recommend.merge(pd.DataFrame(sort_user_predict).reset_index(), on='beer_id')
        recommend = recommend.rename(columns = {nickname:'predict'}).sort_values('predict', ascending=False).head(20)

        result = []

        # 예측한 맥주의 아이디와 예측점수만 리스트로 뽑아냄
        beer_id = recommend['beer_id'].tolist()
        predict = recommend['predict'].tolist()

        # # 예측한 맥주들에 대한 정보들 다 담기
        for bid in beer_id:
            beer_data = get_object_or_404(Beer, id=bid)
            result.append(beer_data)
        serializer = BeerListSerializer(result, many=True)


        data = {
            'beers': serializer.data,
            'predict': predict,
            'review_cnt': review_cnt,
            }


    return Response(data=data)


## 유사한 사용자 추천
@api_view(['GET'])
def similarity(request, nickname):
    # DB에 있는 모든 리뷰 가져오기
    qs = Board.objects.all()
    df = read_frame(qs, fieldnames=['nickname', 'beer_id', 'score'])

    # 사용자가 리뷰를 안 썼을때
    a = df[df.nickname == nickname]
    review_cnt = len(a)

    if review_cnt == 0:
        data = {
        'review_cnt': review_cnt,
        }
    else:
        # DB에 있는 모든 친구 가져오기
        user = get_object_or_404(get_user_model(), nickname = nickname)
        serializer = UserFriendsSerializer(user)
        friends = serializer.data.get('friends')

        # 사용자 기반 협업 필터링 데이터
        table = df.pivot_table('score', index='nickname', columns='beer_id')


        # 해당 사용자가 평가한 맥주 이름 담기
        my_beers = df.loc[df['nickname'] == nickname]
        my_beers = my_beers['beer_id'].tolist()

        # 해당 사용자가 평가한 데이터만 추출
        my_df = pd.DataFrame(table.loc[nickname, my_beers]).T
        # 해당 사용자 이외의 평가 데이터 추출
        other_df = table.loc[:, my_beers].drop(nickname, axis=0)
        # # other_df = other_df.loc[other_df['score'] != -1]

        sim_dict = {}

        for user in other_df.index: 

            sm = [m for m in my_df.columns if math.isnan(other_df.loc[user,m])==False]

            main_n = np.linalg.norm(my_df.loc[nickname,sm])
            user_n = np.linalg.norm(other_df.loc[user,sm])
            prod = np.dot(my_df.loc[nickname,sm], other_df.loc[user,sm])
            similarity=prod/(main_n*user_n) 

            if math.isnan(similarity) == False and user not in friends:
                sim_dict[user]=similarity
            else:
                pass

        sim_item = sim_dict.items()
        sort_sim_item = sorted(sim_item, key=lambda x: x[1], reverse=True)
        recommend_person = sort_sim_item[:5]

        result = []

        for person in recommend_person:
            print(person[0])
            user_data = get_object_or_404(get_user_model(), nickname=person[0])
            result.append(user_data)
        userlist = UserListSerializer(result, many=True)

        cnt = len(recommend_person)
        User = get_user_model()
        all_user = User.objects.all()
        all_user_seri = UserListSerializer(all_user, many=True).data

        random = []

        for u in all_user_seri:
            if cnt < 5:
                if u.get('userID') not in friends and u.get('userID') not in recommend_person:
                    random.append(u)
                    cnt += 1
                else:
                    pass
            else:
                break

        data = {
            'recommend_person' : recommend_person,
            'userlist': userlist.data,
            'random': random
        }

    return Response(data=data)