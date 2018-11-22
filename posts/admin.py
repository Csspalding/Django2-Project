#author Cass November 12th 2018
from django.contrib import admin

# Register your models here.
from .models import Posts

admin.site.register(Posts)