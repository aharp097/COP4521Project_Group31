"""skechwime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('canvas/', include(('canvas.urls', 'canvas'), namespace='canvas')),
    path('lobby/', include(('canvas.urls', 'lobby'), namespace='lobby')),
    path('create_lobby/', include(('canvas.urls', 'create_lobby'), namespace='create_lobby')),
    path('', include(('canvas.urls', 'home'), namespace='home')),
    path('join_lobby/', include(('canvas.urls', 'join_lobby'), namespace='join_lobby')),
    path('login/', include(('canvas.urls', 'login'), namespace='login')),
    path('signup/', include(('canvas.urls', 'signup'), namespace='signup')),
    path('logout/', include(('canvas.urls', 'logout'), namespace='logout')),
    path('__debug__', include(debug_toolbar.urls))
]
