from django.urls import path
from . import views


app_name = 'recommends'
urlpatterns = [
    path('<str:nickname>', views.predict),
    path('similar/<str:nickname>', views.similarity)
    # path('similar/', views.similarity)
]