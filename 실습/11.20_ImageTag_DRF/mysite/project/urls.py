from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # 웹 브라우저에서 로그인이 되게 해줍니다.(테스트에 용이합니다.)
]
