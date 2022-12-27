import pandas as pd

# 합친 데이터를 저장할 데이터프레임
data = pd.DataFrame(data=[], columns=['맥주정보', '검색이름', '맥주이름'])

# 수집한 파일의 개수
files_cnt = 118

for i in range(files_cnt):

    # 해당 경로에서 beer_n_1.csv 형식의 파일들만 수집한 뒤 병합합니다.
    try : 
        tmp = pd.read_csv(r'C:/Users/multicampus/Desktop/PJT/특화/S05P21C205/backend/django/backend/beer_csv/beer_n_'+str(i)+'.csv', index_col=0)
        data = pd.concat([data,tmp])
    # 오류 발생 시 넘어갑니다.
    except :
        print(i, '번째에서 오류가 발생했습니다. 다음 파일로 넘어갑니다.')

# 합친 데이터를 저장합니다.
data.to_csv('전처리전데이터.csv', encoding='utf-8')

# 잘 합쳐졌는지 확인
data = pd.read_csv('전처리전데이터.csv', encoding='utf-8', index_col=0)

data = data[['맥주이름', '맥주정보']]

data.head()
data.info()

data.to_csv('크롤링_원본데이터.csv', encoding='utf-8')