from django.urls import path
from apps.app1 import views

urlpatterns = [
    path('index/', views.index , name ='home'),
    path('gamesList/', views.listgames ,name='games-list'),
]