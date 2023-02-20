"""onlinedanceclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from user import views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('blog/', include('blog.urls')),
    path('event/', include('events.urls')),


    #api
    path('api/blogs/', include('blog.api.urls')),
    path('api/events/', include('popularevents.api.urls')),


]