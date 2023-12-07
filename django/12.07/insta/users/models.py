from django.db import models
from django.contrib.auth.models import AbstractUser

# abstractuser와 abstractbaseuser의 차이
# 전자는 username, password, first_name, last_name, email, is_staff, is_active, is_super
# last_login, date_joined를 기본으로 갖고

# 후자는 password, last_login, is_superuser, username을 기본으로 가진다.
# 초급자에게는 전자가 낫다. 후자쪽이 구현해야될게 너무 많기 때문


class User(AbstractUser):
    intro = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True, upload_to='user/images')