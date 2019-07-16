#author Cass November 12th 2018
from django.urls import path, re_path
from . import views
#from .views import HomePageView

# . import the dot means import all methods in posts.views.py

#My first route and its working, add an index page to POSTS app which is the blog posts, next add a homepage
 
urlpatterns = [
  # local host extension: /posts/ , passes to the index method in  Posts views.py file     
  path('', views.index, name='index'), 
  #path('', HomePageView.as_view(), name='home'),
 

  re_path(r'^details/(?P<id>[0-9])/$', views.details, name= 'details'),
  #Anything that starts with details, the data for each post in the db,  will check P parameter id 
]