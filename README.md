# SWLAB CORE

## Introduction

---
### Computer Science 관련 실습 강의를 위한 온라인 통합 플랫폼

### Main Goal
- 아래 나열되어 있는 강의에 대한 실습 지원
    - 프로그래밍 과목(C,C++,Python,JAVA 등), 시스템프로그래밍, 리눅스, 등
- 교수자 및 학생들에 대한 실습 및 평가 지원

## Install Information

---
### Requirements

- Python 3.9
- Django
- SQL server
- python api requirements
  - refer to requirements.txt

### Install guide

- make DB migration
  ```console
  python manage.py makemigrations
  python manage.py migrate
  ```
- run server
  ```console
  python manage.py runserver 8000
  ```

## Development guide

### Add application 생성

- Add application using console command
  ```console
  python manage.py startapp yourapp
  ```
- SWLAB_core의 settings.py 파일 수정
  - LOCAL_APPS 에 yourapp 추가
- Add 'serializers.py' file
  - 각 app 디렉토리에 serializer.py을 생성하여 활용하는 것이 원칙(필수는 아니지만 필요함)
  - serializers.py 파일은 front-end와의 데이터 직렬화(규칙)을 결정함 
  - Restful API를 통해 front-end와의 연결시 직렬화를 사용하면 데이터 규칙을 정할 수 있음
  - front-end -> API 통신 규칙 예제
     ```python
    from utils.api import serializers
    #user login api와 통신 시 char 타입의 username과 password 변수 규칙 생성
    class UserLoginSerializer(serializers.Serializer):
         username = serializers.CharField()
         password = serializers.CharField()
     ```
  - 이외에도 front-end <- API 통신 규칙도 사용 가능함

### API 생성 및 URL 연결
아래 모든 과정은 'account' app을 참고하면서 보면 이해하기 쉬움

#### API 생성
- application 디렉토리에 'views' 디렉토리 생성
- 아래 두개의 파일 생성 후 API 개발하면 됨
  - default.py : 기본 계정과 관련된 API
  - admin.py : 관리자 계정과 관련된 API
    ```python
      class FirstAPI(APIView):
         def get(self, request):
            print('test')
            print(request)
            return self.success('??????')
    ```

#### URL 연결
URL 연결 과정은 크게 2가지로 구분
- SWLAB_core 의 'url.py' 파일 수정 
- 각 앱의 urls 디렉토리 수정

SWLAB_core 의 url.py 파일 수정

- 'api/' 와 'api/admin'에 각각 새로 추가한 앱의 url 연결
  ```python
    re_path(r"^api/", include("yourapp.urls.defult")),
    re_path(r"^api/admin", include("yourapp.urls.admin")),
  ```

각 앱의 의 url디렉터리 및 url 파일 생성

- yourapp 디렉토리에 urls 디렉토리 생성
- 아래 두개의 파일 생성 후 url 과 views에서 생성한 API 연결
  - default.py : 기본 계정과 관련된 url
  - admin.py : 관리자 계정과 관련된 url
  ```python
    re_path(r"^firstapi/?$", FirstAPI.as_view(), name="first_api"),
    re_path(r"^secondapi/?$", SecondAPI.as_view(), name="second_api"),
  ```