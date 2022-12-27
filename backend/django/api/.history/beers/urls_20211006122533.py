from django.urls import path
from . import views


app_name = 'beers'
urlpatterns = [
    path('list/', views.beer_list),
    path('<int:beer_id>/', views.beer_detail),
    path('list/like/', views.beer_people_like),
    path('search/<str:keyword>/', views.beer_search),
    path('list/<str:type>/', views.beer_list_type),
    path('<int:beer_id>/like/<str:userID>/', views.like),
    path('like/<str:userID>/', views.user_like_list),
    path('most/review/', views.beer_most_review),
    path('best/score/', views.beer_best_score),
]