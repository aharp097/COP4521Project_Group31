from django.urls import path
from views.canvas_view import canvas_view

urlpatterns = [
    path('canvas/', canvas_view, name='canvas'),  # This pattern expects that canvas_view is a view function or class
    path('', canvas_view, name='home'),  # This line handles the root URL
]