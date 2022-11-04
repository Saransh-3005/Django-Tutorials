from unittest import result
from django.urls import path
from . import views

urlpatterns =[
     path('', views.index,name='index'),
      
     path('counter',views.counter,name='counter'),
     path('blogs',views.blog,name='blogs'),
     path('weather',views.weather,name='weather'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('signup',views.signup,name='signup'),
     path('result', views.result,name='result')
] 