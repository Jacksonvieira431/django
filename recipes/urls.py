from django.urls import path
from recipes import views

urlpatterns = [
    path('', views._home),
    path('contato/', views._contato),
    path('sobre/', views._sobre)
]