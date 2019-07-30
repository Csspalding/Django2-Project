#author Cass July 8th 2019

from django.urls import path, re_path

from . import views

# . import the dot means import all methods in cupcakecode views.py

 
urlpatterns = [
  # local host extension: /CupCakeCode/ , passes to the home method in cupcakecode dir views.py file     
  
  path('', views.home, name='home'),
  path('home', views.home, name='home'),
  path('about', views.about, name='about'),
  path('info', views.info, name='info'),
  path('contact', views.contact, name='contact'),
  path('cup_cake', views.cup_cake, name='cup_cake_app'),
  

  
]