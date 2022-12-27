from django.urls import path
from . import views


app_name = 'boards'
urlpatterns = [
    path('<int:beer_id>/review/', views.board_list),
    path('<str:userID>/review/', views.user_board_list),
    path('<int:beer_id>/review/create/', views.board_create),
    path('<int:beer_id>/review/<int:board_id>/', views.board_detail),
    path('<int:beer_id>/review/<int:board_id>/update/', views.board_update),
    path('<int:beer_id>/review/<int:board_id>/delete/', views.board_delete),
]