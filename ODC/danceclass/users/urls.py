from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('signup/', views.signup, name='signup'),  
    path('userSignup/', views.userSignup, name='userSignup'),  
    path('login', views.login, name='login'),  
    path('logout/', views.logout, name='logout'), 
    path('admin-panel/', views.adminDashboard, name='adminDashboard'),  
    path('blog/', views.blog, name='blog'),
    path('blogtitle/', views.blogtitle, name='blogtitle'),  
    path('blogtitle1/', views.blogtitle1, name='blogtitle1'),  

]

