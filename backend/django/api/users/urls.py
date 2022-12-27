from django.urls import path
from . import views


app_name = 'users'
urlpatterns_user = [
    path('register/', views.register),
    path('register/userID/<str:userID>/', views.register_check_userID),
    path('register/nickname/<str:nickname>/', views.register_check_nickname),
    path('deregister/<str:userID>/', views.deregister),
    path('user/list/', views.user_list),
    path('user/<str:userID>/detail/', views.user_info),
    path('user/<str:userID>/update/<str:column>/', views.user_info_update),
    path('login/', views.login),
    path('user/search/<str:keyword>/', views.user_search),
]

urlpatterns_friend = [
    path('user/<str:userID>/friends/', views.friends_list),
    path('user/<str:userID>/friends/add/', views.friends_add),
    path('user/from/<str:fromA>/to/<str:toB>/', views.request_friend),
    path('user/from/<str:fromA>/to/<str:toB>/delete/', views.friends_remove),
    path('user/<str:userID>/where/', views.friends_where),
]

urlpatterns = urlpatterns_user + urlpatterns_friend