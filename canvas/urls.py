from django.urls import path
from . import views

urlpatterns = [
    path('lobby/<str:lobby_name>/', views.lobby_view, name='lobby'),
    path('', views.home_view, name='home'),
    path('create_lobby/', views.create_lobby, name='create_lobby'),
    path('join_lobby/', views.join_lobby, name='join_lobby'),
    path('canvas/<str:lobby_name>/', views.canvas_view, name='canvas'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout')
]
