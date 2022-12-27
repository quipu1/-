import pandas as pd

### 맥주 데이터 최종본

beers_data = pd.read_csv('beers.csv', index_col=0)
beer_class_data = pd.DataFrame(beers_data['class']).groupby(['class']).size()
# beer_class_data = pd.DataFrame(beer_class_data.groupby(['class']))
class_data = pd.DataFrame(beer_class_data).reset_index()
class_data.rename(columns={0:'class_cnt'}, inplace=True)

# print(class_data)

class_data.to_csv('beer_class.csv', encoding='utf-8')
