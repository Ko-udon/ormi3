과제 내용
```
# Access Token이 유효한 경우에만 접근이 가능한 마이페이지를 만들어주세요.

1. 로그인하여 Access Token을 발급받습니다.
2. 마이페이지 접속시 header에 Access Token을 담아보냅니다. Access Token이 유효한 경우에만 마이페이지에 접근이 가능합니다.
3. 마이페이지에 접속하면(포스트맨 또는 다른 API 툴로 하셔도 됩니다.) "반갑습니다, {유저이메일}님!"이 화면에 출력되도록 해주세요.

# 구현되어야할 엔드 포인트는(API) 아래와 같습니다.

/account/join # 회원가입
/account/login # 로그인
/account/logout # 로그아웃
/account/mypage # 로그인한 사용자만 확인가능
```

___
## 프로젝트 생성

프로젝트를 생성할 폴더를 만들고 가상환경과 필요한 패키지를 설치하자

```
python -m venv vevn # 가상환경 

.\venv\Scripts\activate # 가상환경 실행

pip install django # django 설치

```

django 프로젝트를 만들고 필요한 패키지를 설치한다.
requirements.txt 파일은 아래와 같다.


```
django-admin startproject tutorialdjango . # 프로젝트 생성

pip install -r requirements.txt

```
requirements.txt 파일은 아래와 같다.
```
asgiref==3.7.2
certifi==2023.7.22
cffi==1.16.0
charset-normalizer==3.3.2
cryptography==41.0.5
defusedxml==0.7.1
dj-rest-auth==2.2.4
Django==4.0.3
django-allauth==0.50.0
djangorestframework==3.13.1
djangorestframework-simplejwt==5.1.0
idna==3.4
oauthlib==3.2.2
pycparser==2.21
PyJWT==2.8.0
python3-openid==3.2.0
pytz==2023.3.post1
requests==2.31.0
requests-oauthlib==1.3.1
sqlparse==0.4.4
typing_extensions==4.8.0
tzdata==2023.3
urllib3==2.0.7

```
___
## tutorialdjango > settings.py
```python
# 추가
from datetime import timedelta

# 추가
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',

    # 설치한 라이브러리들
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

# 추가
AUTH_USER_MODEL = 'accounts.CustomUser'

# dj-rest-auth
REST_USE_JWT = True # JWT 사용 여부
JWT_AUTH_COOKIE = 'my-app-auth' # 호출할 Cookie Key 값
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' # Refresh Token Cookie Key 값

# django-allauth
SITE_ID = 1 # 해당 도메인 id
ACCOUNT_UNIQUE_EMAIL = True # User email unique 사용 여부
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username' # 사용자 이름 필드 지정
ACCOUNT_USERNAME_REQUIRED = True # User username 필수 여부
ACCOUNT_EMAIL_REQUIRED = True # User email 필수 여부
ACCOUNT_AUTHENTICATION_METHOD = 'email' # 로그인 인증 수단
ACCOUNT_EMAIL_VERIFICATION = 'none' # email 인증 필수 여부

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # AccessToken 유효 기간 설정
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # RefreshToken 유효 기간 설정
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

___
## tutorialdjango > urls.py

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("accounts.urls"))
]
```
___
## accounts > models.py
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

GENDER_CHOICES = (
    ('male', '남자'),
    ('female', '여자'),
)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=6, blank=False, default='이름')
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email

```
___
## accounts > manages.py
```python
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
```
___
## accounts > urls.py
```python
from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('join/', include('dj_rest_auth.registration.urls')),
    path('mypage', view=views.mypage),
]
```
___
## accounts > view.py

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mypage(request):
    content = {'message': '반갑습니다,' + str(request.user.username) + '님!'}
    
    return Response(content)
 ```
 
 ___
 
 ## 테스트
 
 ### 회원가입
![](https://velog.velcdn.com/images/eastfriend22/post/527fd9c3-b20a-4b80-b6b8-d45a2c36c940/image.png)

![](https://velog.velcdn.com/images/eastfriend22/post/dad0be3c-5fb0-4d3d-8ecd-e67ee028a31b/image.png)


### 로그인
가입이 성공했고, 로그인을 해보자
![](https://velog.velcdn.com/images/eastfriend22/post/7be434c8-cf3e-4b6d-8192-a08e095dd59d/image.png)
![](https://velog.velcdn.com/images/eastfriend22/post/e05f1e90-f036-475a-9f1c-885a08f5b3e4/image.png)

### 마이페이지

마이페이지는 Thunder Client로 호출해보자
![](https://velog.velcdn.com/images/eastfriend22/post/3765a6cd-a3ec-492a-bc9c-c96a40588cdf/image.png)







 





