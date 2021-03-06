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


from posts import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    #path('', views.home, name='home'), # sets the url localhost:8000 homepage
    path('', include('posts.urls')), #sets homepage to our trial app posts page for now change later to a home page 
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),#this include method needs to be imported
]
