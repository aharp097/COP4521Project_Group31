from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.lobby_view, name='lobby'),
    path('', views.home_view, name='home'),
    path('create_lobby/', views.create_lobby, name='create_lobby'),
    path('join_lobby/', views.join_lobby, name='join_lobby'),
    path('canvas/<int:lobby_id>/', views.canvas_view, name='canvas'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout')
]