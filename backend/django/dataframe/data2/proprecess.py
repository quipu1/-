import pandas as pd
import re

data = pd.read_csv('크롤링_원본데이터.csv', encoding='utf-8', index_col=0)

# 맥주정보 Raw 데이터값
# print(data['맥주정보'].iloc[0])


### 문자열 분리하기
# tmp 변수에 카피
tmp = data.copy()

# \n 개행문자 기준으로 분리
tmp['맥주정보'] = tmp['맥주정보'].str.split('\n')
tmp['맥주정보']

# 분리된 스트링 값 확인 -> List로 변환됨
print(tmp['맥주정보'].iloc[0])


### 좋아요 수 삭제
# 새로운 데이터 프레임 ttmp에 copy()후 전처리 하겠습니다.
ttmp = tmp.copy()
# 맥주정보 리스트 출력 : 좋아요 수가 기록된 유저 정보
# print(ttmp['맥주정보'].iloc[0])

# 전체 데이터프레임에서 좋아요가 1개인 것 찾아서 맨 뒤에 것 삭제
ttmp['맥주정보'] = ttmp['맥주정보'].apply(lambda x : x if x[-2]=='Overall' else x[:-1] )

# 맥주정보에서 0,1,2,3번째 리스트 요소와 뒤에서부터 10개의 리스트요소(평점값들)추출
ttmp['맥주정보'] = ttmp['맥주정보'].apply(lambda x : x[:4]+x[:-11:-1])

# 좋아요 수가 정상적으로 삭제됨
# print(ttmp['맥주정보'].iloc[0])

# 맨 첫번째 리스트 요소에 ID 저장
# 그 뒤로는 뒤에서부터 각 평가값 저장
ttmp['ID'] = ttmp['맥주정보'].apply(lambda x: x[0])
ttmp['Aroma'] = ttmp['맥주정보'].apply(lambda x: x[-2])
ttmp['Appearance'] = ttmp['맥주정보'].apply(lambda x: x[-4])
ttmp['Flavor'] = ttmp['맥주정보'].apply(lambda x: x[-6])
ttmp['Mouthfeel'] = ttmp['맥주정보'].apply(lambda x: x[-8])
ttmp['Overall'] = ttmp['맥주정보'].apply(lambda x: x[-10])

# 리스트의 1,2,3번째 요소만(평점날짜 or 이상한 값) 뽑아오기
ttmp['맥주정보'] = ttmp['맥주정보'].apply(lambda x:x[1:4])
ttmp['길이'] = ttmp['맥주정보'].apply(lambda x:len(x))

# 결과 확인
# print(ttmp.head(3))


### 평점|날짜 데이터 골라내기
reg = re.compile('[0-9]+.+[0-9]+[A-Za-z0-9]*')

ttmp['맥주정보'] = ttmp['맥주정보'].apply(lambda x: x[0] if reg.match(x[0]) else (x[1] if reg.match(x[1]) else x[2]))

### 평점과 날짜 데이터 분리
# 평점은 0번째부터 3번째, 날짜는 그 이후 문자열로 처리
ttmp['평점'] = ttmp['맥주정보'].apply(lambda x : x[:3])
ttmp['날짜'] = ttmp['맥주정보'].apply(lambda x : x[3:])

# print(ttmp.head(3))

###
# 컬럼명 변경
ttmp.columns = ['맥주', '맥주정보', '길이', '아이디', 'Aroma', 'Appearance', 'Flavor', 'Mouthfeel', 'Overall', '평점', '날짜']

# 필요한 컬럼만 추출
ttmp = ttmp[['아이디', '맥주', '날짜', '평점', 'Aroma', 'Appearance', 'Flavor', 'Mouthfeel', 'Overall']]

ttmp.평점.unique()
ttmp.Aroma.unique()

# 세부 리뷰 값이 '-'가 아닌 데이터만 저장
ttmp = ttmp[ttmp['Aroma']!='-']
ttmp = ttmp[ttmp['Appearance']!='-']
ttmp = ttmp[ttmp['Flavor']!='-']
ttmp = ttmp[ttmp['Mouthfeel']!='-']
ttmp = ttmp[ttmp['Overall']!='-']
ttmp[ttmp['Aroma']=='-']

# ttmp.info()

# 수치형 데이터는 실수로 변환 : pd.to_numeric() 함수 사용
ttmp['평점'] = pd.to_numeric(ttmp['평점'])
ttmp['Aroma'] = pd.to_numeric(ttmp['Aroma'])
ttmp['Appearance'] = pd.to_numeric(ttmp['Appearance'])
ttmp['Flavor'] = pd.to_numeric(ttmp['Flavor'])
ttmp['Mouthfeel'] = pd.to_numeric(ttmp['Mouthfeel'])
ttmp['Overall'] = pd.to_numeric(ttmp['Overall'])
# 중복된 행들을 제거합니다.
ttmp.drop_duplicates(keep='first', inplace=True)

# 최종 데이터 확인
# ttmp.info()

# 최종 데이터 값 분포 확인
# print(ttmp.describe())


### 저장
ttmp.to_csv('전처리후데이터.csv', encoding='utf-8')