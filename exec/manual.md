# 포팅 매뉴얼



## 목차

1. gitlab 소스 클론 이후 빌드 및 배포할 수 있는 작업 문서

   (1) 사용한 JVM, 웹서버, WAS 제품 등의 종류와 설정값, 버전 (IDE버전 포함) 기재

   (2) 빌드 시 사용되는 환경 변수 등의 주요 내용 상세 기재

   (3) 배포 시 특이사항 기재

   (4) 데이터베이스 접속 정보 등 프로젝트(ERD)에 활용되는 주요 계정 및 프로퍼티가 정의된 파일 목록

2. 프로젝트에서 사용되는 외부 서비스 정보 문서

   (1) 소셜인증, 포통 클라우드, 코드 컴파일 등에 활용된 '외부 서비스' 가입 및 활용에 필요한 정보

3. 데이터베이스 덤프 파일 최신본

4. 시연 시나리오(스크립트 포함)



-----



### 1. gitlab 소스 클론 이후 빌드 및 배포할 수 있는 작업 문서

#### (1) 사용한 JVM, 웹서버, WAS 제품 등의 종류와 설정값, 버전 (IDE버전 포함) 기재

* nginx : 1.18.0 (Ubuntu)

* gunicorn : 20.1.0

* daphne

#### (2) 빌드 시 사용되는 환경 변수 등의 주요 내용 상세 기재



#### (3) 배포 시 특이사항 기재

* ***nginx*** 설정

경로 : /etc/nginx/sites-enabled/default

```
upstream your_web_gunicorn {
    server localhost:8000;
}
upstream your_channel_daphne {
    server localhost:8001;
}

server {

        root /home/ubuntu/S05P21C205/frontend/dist;
		index index.html index.htm index.nginx-debian.html;
		
        server_name j5c205.p.ssafy.io;

        location / {
                try_files $uri $uri/ /index.html;
        }

        location /api/ {
                include proxy_params;
                proxy_pass http://unix:/home/ubuntu/S05P21C205/backend/django/api/api.sock;
        }

        location /static/ {
                alias /home/ubuntu/S05P21C205/backend/django/api/staticfiles/;
        }

        location /ws {
                proxy_pass http://your_channel_daphne;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                proxy_redirect off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Host $server_name;
        }

        listen 80; # managed by Certbot

        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/j5c205.p.ssafy.io/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/j5c205.p.ssafy.io/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
```



* ***gunicorn*** 설정

경로 : /etc/systemd/system/gunicorn.service

```
[Unit]
Description=ssafy5 c205
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/S05P21C205/backend/django/api
ExecStart=/home/ubuntu/S05P21C205/backend/django/api/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/S05P21C205/backend/django/api/api.sock config.wsgi:application

[Install]
WantedBy=multi-user.target
```



* ***daphne*** 설정

경로 : /etc/systemd/system/daphne.service

```
[Unit]
Description=daphne server script
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/S05P21C205/backend/django/api
Environment=DJANGO_SETTINGS_MODULE=config.settings.base
ExecStart=/home/ubuntu/S05P21C205/backend/django/api/venv/bin/daphne -b 127.0.0.1 -p 8001 config.asgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```



* 채팅 기능 - 도커의 redis 컨테이너를 backing store로 사용

ubuntu 환경에 도커 설치 후 아래 실행

```
$ docker run -p 6379:6379 -d redis:5
```



#### (4) 데이터베이스 접속 정보 등 프로젝트(ERD)에 활용되는 주요 계정 및 프로퍼티가 정의된 파일 목록

* db 접속정보

`backend > api > my_settings.py`

```
# MYSQL 연동
DATABASES = { 
	'default': { 
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'beer', 
        'USER': 'root', 
        'PASSWORD': 'root', 
        'HOST': 'j5c205.p.ssafy.io', 
        'PORT': '3306', 
        }
}

SECRET_KEY = 'django-insecure-mu&b&31(*bw5wsj$pgk#ulj&)!j%haj748a+!^c^m-wgb7r4g!'
```



<BR>

### 2. 프로젝트에서 사용되는 외부 서비스 정보 문서

* 카카오맵 API

  *  kakao developers > '내 어플리케이션' > 카카오 맵 > 허용할 url 설정

    ```
    http://j5c205.p.ssafy.io
    ```

  * 사용할 html 코드에서 js 인증키를 불러온 뒤 사용

    ```js
    <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=JS인증키"></script>
    ```

    

    



<br>

### 3. 데이터베이스 덤프 파일 최신본

* 맥주 리뷰 : revies.csv
* 맥주 종류 및 설명 : beers.csv

<br>

## 4. 시연 시나리오

**Beer**

- 전체 맥주/상세 맥주

  ![image-20211008000347538](/images/image-20211008000347538.png)

  ![image-20211008000410324](/images/image-20211008000410324.png)

  전체 맥주 목록에서 맥주를 클릭하면 상세 맥주 정보를 볼 수 있습니다.



- 맥주 검색

  ![image-20211008000549570](/images/image-20211008000549570.png)

  화면 상단의 검색창을 통해 맥주를 검색할 수 있습니다.

  

- 맥주 찜하기

  ![image-20211008000653673](/images/image-20211008000653673.png)

  ![image-20211008000743413](/images/image-20211008000743413.png)

맥주 상세 정보에서 찜하기를 누르면 내가 찜한 맥주 목록에서 해당 맥주가 보여집니다.



- 맥주 추천 (협업 필터링X)

  ![image-20211008000932481](/images/image-20211008000932481.png)

유저들이 가장 리뷰를 많이 쓴 맥주, 찜이 많은 맥주, 맥주 score가 가장 높은 맥주 최대 6개를 메인 페이지에서 보여줍니다.

-

--------------------



**User**

- 회원가입

  ![image-20211007234902561](/images/image-20211007234902561.png)

  아이디와 닉네임이 모두 기존의 유저와 겹치지 않을 경우만 회원가입이 가능합니다.

  

- 회원가입 - 선호도

  ![image-20211007235955499](/images/image-20211007235955499.png)

  자신이 좋아하는 맥주 종류를 세 가지 선택할 수 있습니다. 

  잘 모르는 경우는 "모름"을 선택할 수 있고,

  마우스를 올리면 상세 설명과 대표 맥주를 알 수 있습니다.

  

- 회원가입 - 선호도

  ![image-20211008000218802](/images/image-20211008000218802.png)

  앞에서 선택한 취향 기반으로, 모르는 것을 고를 경우 대표적인 맥주 몇 가지로 이상형 월드컵 형식의 선호도 조사를 한 번 더 조사합니다.

  여기서 선택된 맥주에는 5점이 부여되어, 첫 추천에 기반이 됩니다.



- 회원 정보 수정

![image-20211008001052002](/images/image-20211008001052002.png)

![image-20211008002339583](/images/image-20211008002339583.png)

회원 정보 수정란에서 닉네임/선호도 수정 및 회원탈퇴가 가능합니다.



-----------



**Board**

- 맥주 별점 + 리뷰

  ![image-20211008002703764](/images/image-20211008002703764.png)

  맥주 상세 페이지에서 간단히 댓글 형식으로 별점과 함께 마셔본 맥주에 대한 평가를 남길 수 있습니다. 여기에 남긴 리뷰는 점수가 사용자 맞춤 맥주를 추천할 때 이용됩니다.



------------------------



**Feed**

- 피드 작성 / 피드 댓글 작성

  ![image-20211008003652200](/images/image-20211008003652200.png)

  자유롭게 피드를 쓰고 다른 사용자와 댓글을 주고받을 수 있습니다.



------------



**Chat**

- 채팅

  ![image-20211008005022758](/images/image-20211008005022758.png)

가입한 유저들끼리 상호 채팅이 가능합니다. 

유사도를 통해 추천받은 유저와 혹은 거리가 가까운 유저와 채팅을하여 맥주 친구를 찾는 기능입니다.



-----------



**Recommend**

- 맥주 추천 기능

  ![image-20211008010000444](/images/image-20211008010000444.png)

사용자들이 작성한 리뷰를 기반으로, 높은 점수를 줄 것으로 예상되는 맥주들을 추천해줍니다.



- 빅데이터 기반 친구 추천 기능 (CSS 오류)

  ![image-20211008010015173](/images/image-20211008010015173.png)

사용자들이 작성한 리뷰를 기반으로, 자신과 맥주 점수가 유사한 유저들을 추천합니다.



- 위치 기반 친구 추천 기능

  ![image-20211008010748297](/images/image-20211008010748297.png)

위치를 동의한 사용자들은 반경 1km 이내의 사용자들에게 자신의 위치를 보여줍니다.

가까이 살고있는 유저와 맥주 한 잔을 하고 싶을 경우 맥주팟에서 사람들의 위치를 확인하고, 

채팅을 이용해 약속을 잡아 맥주를 마실 수 있습니다.

