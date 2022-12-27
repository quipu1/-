import pandas as pd

### 맥주 데이터 최종본

beer_data = pd.read_csv('전체맥주리스트3.csv', encoding='utf-8', index_col=0)
flavor_data = pd.read_csv('전체맥주세부맛.csv', encoding='utf-8', index_col=0)

flavor_data = flavor_data.reset_index()

flavor_data.rename(columns={'맥주':'beer_eng_name'}, inplace=True)
print(flavor_data)

beers_data = pd.merge(beer_data, flavor_data, on='beer_eng_name', how='left')


beers_data.rename(columns={'review_score':'score', 'Aroma':'aroma', 'Appearance':'appearance', 'Mouthfeel':'mouthfeel', 'Flavor':'flavor'}, inplace=True)

# beers_data = beers_data.rename_axis('id').reset_index()

# beers_data.to_csv('beers.csv', encoding='utf-8')

# beers_data.info()
# print(beers_data)
