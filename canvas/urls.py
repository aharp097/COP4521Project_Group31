from django.urls import path
from . import views

urlpatterns = [
    path('', views.canvas_view, name='canvas'),
    path('lobby/', views.lobby_view, name='lobby'),
    path('', views.canvas_view, name='home'),
]