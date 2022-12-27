import csv
import os
import django
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")   # 1. 여기서 프로젝트명.settings입력
django.setup()

# 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과

### beer 테이블 데이터 ###
from api.beers.models import Beer

# codelist = defaultdict(str)
# tourdetaillist = defaultdict(str)
CSV_PATH = './beers.csv'   # 3. csv 파일 경로
    
    
with open(CSV_PATH, newline='') as csvfile:   # 4. newline =''
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        print(row)
        Beer.objects.create(
            beer_kor_name = row['beer_kor_name'],
            beer_eng_name = row['beer_eng_name'],
            class_field = row['class'],
            score = row['score'],
            country = row['country'],
            description = row['description'],
            aroma = row ['aroma'],
            appearance = row['appearance'],
            flavor = row['flavor'],
            mouthfeel = row['mouthfeel']
        )