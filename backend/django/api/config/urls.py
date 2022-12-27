"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework import routers, permissions


schema_view = get_schema_view(
    openapi.Info(
        title="비어있는 편의점", # 타이틀
        default_version='v1', # 버전
        description="비어있는 편의점 API 문서", # 설명
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="blessisu@naver.com"),
        license=openapi.License(name=""),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns_swagger = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]

urlpatterns_function = [
    path('api/admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/beer/', include('boards.urls')),
    path('api/beer/', include('beers.urls')),
    path('api/feed/', include('feeds.urls')),
    path('api/recommend/', include('recommends.urls')),
    path('api/chat/', include('chat.urls')),
]

urlpatterns = urlpatterns_swagger + urlpatterns_function 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)