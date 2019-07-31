#author Cass July 2019
from django.urls import path, re_path

from . import views

# . import the dot means import all methods in posts.views.py

#My first route test and its working, add an index page to POSTS app which is the blog posts
 
urlpatterns = [
  # local host extension: /posts/ , passes to the index method in  Posts views.py file     
  path('', views.index, name='index'), 

  re_path(r'^details/(?P<id>[0-9])/$', views.details, name= 'details'),
  #Anything that starts with details, the data for each post in the db,  will check P parameter  Django gives an automatic id which autoincrements in the datebase as each new post is added to the blog 
]