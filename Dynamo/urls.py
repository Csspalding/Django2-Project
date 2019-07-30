"""Dynamo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

from CupCakeCode import views 
from posts import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    #django.urls 'include' method needs to be imported see above imports
    path('', include('CupCakeCode.urls')), # sets the url localhost:8000  as the home page
    
    #path('home/', include('CupCakeCode.urls')),
    path('about/', include('CupCakeCode.urls')),
    path('info/', include('CupCakeCode.urls')),
    #todo the app currently test page
    path('cup_cake/', include('CupCakeCode.urls')),
    path('contact/', include('CupCakeCode.urls')),

    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]
