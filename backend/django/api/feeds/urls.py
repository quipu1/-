from django.urls import path
from . import views


app_name = 'feeds'
urlpatterns = [
    path('list/', views.feed_list),
    path('list/<str:userID>/', views.user_feed_list),
    path('create/', views.feed_create),
    path('<int:feedID>/', views.feed_detail),
    path('<int:feedID>/update/', views.feed_update),
    path('<int:feedID>/delete/', views.feed_delete),
    path('<int:feedID>/comment/', views.comment_list),
    path('<int:feedID>/comment/create/', views.comment_create),
    path('<int:feedID>/comment/<int:commentID>/update/', views.comment_update),
    path('<int:feedID>/comment/<int:commentID>/delete/', views.comment_delete),
]