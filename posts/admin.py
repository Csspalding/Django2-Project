#author Cass July 2019
from django.contrib import admin

# Register your models here.
from .models import Posts


admin.site.register(Posts)