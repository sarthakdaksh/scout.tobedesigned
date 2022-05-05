from django.contrib import admin
from django.urls import path
from function import views

urlpatterns = [
    path('', views.firstpage, name = 'home'),
    path('home', views.firstpage, name = 'home'),
    path('second', views.secondpage, name = 'browse'),
    path('third', views.thirdpage, name = 'results'),
    path('fourth', views.fourthpage, name = 'userprofile'),
]
