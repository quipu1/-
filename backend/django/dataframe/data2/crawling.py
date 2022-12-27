import pandas as pd
import numpy as np
import time
# import openpyxl

import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

# 맥주 목록들
beer_list = [
    # 'Kronenbourg 1664 Blanc',
    # 'Kabrew Gyeongbokgung Royal Pride IPA',
    # 'ARK Seoulite Ale',
    # 'Kabrew Kumiho India Pale Ale',
    # 'Kabrew Kumiho Peach Ale',
    # 'Goose Island Goose IPA',
    # 'Goose Island Duck Duck Goose',
    # 'Goose Island Matilda',
    # 'Goose Island Bourbon County Stout',
    # 'Goose Island Sofie',
    # 'Goose Island Summertime',
    # "Goose Island Pepe Nero",
    # "Goose Island Honkers Ale",
    # "Goose Island 312 Urban Wheat Ale",
    # "Guinness Draught",
    # "Guinness Extra Stout (North America)",
    # "Guinness Foreign Extra Stout",
    # "Guinness Black Lager",
    # "Kirin Lager",
    # "Kirin Ichiban",
    # "Kabrew Namsan Mountain Premium Citra Ale",
    # "Budweiser",
    # "Budweiser Select",
    # "Budweiser Budvar",
    # "Budweiser Budvar Dark",
    # "Desperados",
    # "Desperados Red",
    # "Hite D (Dry Finish)",
    # "Lagunitas India Pale Ale (IPA)",
    # "Lagunitas DayTime",
    # "Lagunitas Maximus IPA",
    # "Tsingtao Laoshan 4.0% 10°P",
    # "Tsingtao Laoshan 4.7% 11°P",
    # "Leffe Brune",
    # "Mango Lingo",
    # "Hite Prime Max",
    # "Magners Juicy Apple",
    # "Miller Genuine Draft (MGD)",
    # "Miller Lite",
    # "Miller Chill Chelada Style",
    # "Miller High Life",
    # "San Miguel Pale Pilsen",
    # "Sapporo Draft Beer",
    # "Sapporo Reserve",
    # "Sapporo premium lager",
    # "Suntory The Premium Malt's",
    # "Suntory The Premium Malt's Kaoru Ale",
    # "Spaten Münchner München",
    # "Spaten Oktoberfest Ur-Märzen",
    # "Spaten Optimator",
    # "Stella Artois",
    # "Singha Draft",
    # "Somersby Apple Cider",
    # "Warsteiner Premium Verum",
    # "Warsteiner Premium Dunkel",
    # "Beck's",
    # "Beck's Dark",
    # "BrewDog Punk AF",
    # "BrewDog Punk IPA (5.6%)",
    # "Blue Moon Belgian White",
    # "Asahi Super Dry",
    # "Asahi Super Dry Black",
    # "Asahi Clear Prime Rich",
    # "Apple Fox",
    # "Edelweiss Weissbier Snowfresh",
    # "Erdinger Weissbier",
    # "Sapporo Yebisu",
    # "Isul Tok Tok",
    # "Hite Black Beer Stout",
    # "Egger Naturtrüber Zitronenradler",
    # "Egger Grapefruit Radler",
    # "Jeju Baengnokdam Ale",
    # "Jeju Seongsan Ilchulbong Ale",
    # "Jeju Wit Ale",
    # "Jeju Pellong Ale",
    # "Cass Light",
    # "Cass Fresh",
    # "Carlsberg Pilsner",
    # "Corona Extra",
    # "Corona Light",
    # "Kozel Černý (Dark) 10°",
    # "Kozel Premium Lager 12°",
    # "Queen's Ale Blonde Type",
    # "Queen's Ale Extra Bitter Type",
    # "Kloud Original Gravity",
    # "Tiger Beer",
    # "Tiger Radler Lemon",
    # "Terra",
    # "Tsingtao",
    # "Tsingtao Wheat Beer",
    # "Tsingtao Draft Beer 11º (Pure Draft Beer)",
    # "Paulaner Original Münchner Hell (Premium Lager)",
    # "Paulaner Oktoberfest Bier (Wiesn Bier)",
    # "Paulaner Salvator",
    # "Paulaner Hefe-Weissbier",
    # "Patagonia",
    # "Patagonia Amber Lager",
    # "Patagonia Weisse",
    # "Patagonia Bohemian Pilsener",
    # "Peroni",
    # "Happoshu Filgood",
    # "FiLite",
    # "Filite Fresh Cool & Clear",
    # "Filite Weizen",
    # "Pilsner Urquell",
    # "Fitz Super Clear",
    # "Harbin Beer",
    # "Heineken",
    # "Heineken 0.0",
    # "Heineken Dark Lager",
    # "Hite Beer",
    # "Hite Extra Cold",
    # "Hite Zero",
    "Hoeg",
    # "Hoegaarden Rosée",
    # "Hop House 13 Lager",
    # "Kabrew Hoptandu IPA",
]

# 데이터프레임으로 저장
beer_list = pd.DataFrame(data=beer_list, columns=['검색이름'])

# 데이터 프레임 생성
data = pd.DataFrame(data=[], columns=['맥주정보', '검색이름', '맥주이름'])

# chromedriver.exe 파일 경로 설정
chromedriver = r"C:/Users/multicampus/chromedriver_win32/chromedriver.exe"
# 크롤링 할 경로 설정
url = 'https://www.ratebeer.com/search?tab=beer'

# 셀레니움으로 웹브라우저를 오픈합니다.
driver = webdriver.Chrome(chromedriver)
driver.get(url)
driver.set_window_size(900, 900)
time.sleep(1)


def crawl(driver, beer, data, k):
    # 데이터 프레임 생성
    data = pd.DataFrame(data=[], columns=['맥주정보', '검색이름', '맥주이름'])

    # url open
    print('url_open... {0} 맥주 데이터를 수집합니다..'.format(beer))
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    driver.set_window_size(900, 900)

    # 맥주 검색
    # 셀레니움이 화면을 인식할 시간 주기
    time.sleep(2)
    element = driver.find_element_by_xpath('''//*[@id="root"]/div[2]/header/div[2]/div[1]/div[2]/div/div/input''')
    time.sleep(3)
    element.click()
    time.sleep(2)
    element.send_keys(beer)
    time.sleep(3)

    # 상품 선택
    driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div[2]/div[1]/div[2]/div/div[2]/a[1]/div/div[2]').click()

    # 상품 이름 수집
    time.sleep(3)
    beer_name = driver.find_element_by_css_selector('.MuiTypography-root.Text___StyledTypographyTypeless-bukSfn.pzIrn.text-500.colorized__WrappedComponent-hrwcZr.hwjOn.mt-3.MuiTypography-h4').text

    error_cnt = 0

    while 1:
        try :
            # 전체 리뷰 개수 수집
            time.sleep(3)
            string = driver.find_element_by_class_name('MuiTypography-root.Text___StyledTypographyTypeless-bukSfn.pzIrn.text-500.colorized__WrappedComponent-hrwcZr.hwjOn.MuiTypography-h6').text

            # ,가 포함되어 있는지에 대한 로직
            extract = re.compile('[0-9]*,*[0-9]+')
            str_num = extract.findall(string)
            str_num = str_num[0]

            print('성공... while문을 탈출합니다.')
            break
        except :
            print('오류 발생.. 다시 시작합니다.')

            error_cnt += 1

            if error_cnt == 5:
                print('연속된 오류로 다음 맥주로 넘어갑니다...')
                return

    if ',' in str_num:
        str_num = str_num.split(',')
        str_num = int(str_num[0]+str_num[1])
        num = str_num
    else:
        num = int(str_num)

    # Score breakdown 클릭
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[2]/div[1]/div[2]')
    time.sleep(3)

    driver.execute_script("arguments[0].click();", element)

    # 수집할 Page 수 계산
    if num > 500:
        num = 450
        page_num = num // 15
    else:
        page_num = num // 15 + 1


    for i in range(page_num):
        print(i+1, '번째 페이지입니다.')

        # 전체 맥주 정보를 통째로 수집
        time.sleep(3)
        beer_info = driver.find_elements_by_css_selector('.px-4.fj-s.f-wrap')

        tmp = []

        # 수집한 것을 데이터프레임에 저장
        for i in range(len(beer_info)):
            tmp.append(beer_info[i].text)

        # 한 페이지동안 수집한 것을 기존 data 프레임에 합침
        tmp = pd.DataFrame(data=tmp, columns=['맥주정보'])
        tmp['맥주이름'] = beer_name
        tmp['검색이름'] = beer
        data = pd.concat([data, tmp])

        # 다음 페이지로 넘어가기
        # div, span, title 태그 후 속성은 class 외에도 사용 가능
        try :
            element = driver.find_element_by_xpath('//button[@title="Next page"]/span[@class="MuiIconButton-label"]')
            time.sleep(3)
            driver.execute_script("arguments[0].click();", element)
        except:
            print('마지막 페이지입니다.')

    # 데이터가 중복 수집될 경우 리뷰 수 만큼만 Cut
    if num != len(data):
        data = data[:num]

    print('리뷰수 : ', num, '수집된 리뷰수 : ', len(data))

    # data = ILLEGAL_CHARACTERS_RE.sub(r'', data)

    # 데이터를 csv, excel 파일로 저장합니다.
    result = pd.merge(data, beer_list, on='검색이름', how='left')
    result.to_csv("beer_n_"+str(k+114)+".csv", encoding='utf-8')
    # result.to_excel("beer_n_"+str(k)+".xlsx")

    driver.quit()

    return result

for k in range(len(beer_list)):
    result = crawl(driver, beer_list['검색이름'].iloc[k], data, k)