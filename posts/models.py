#author Cass July 2019
from django.db import models
from datetime import datetime

# Create your models here.
    

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
#To show the title of each of the items listed in Posts instead of default Post Object 1,2,3 in our model
    def __str__(self):
        return self.title
    #to save the model unit eg 'Blog' as a plural, (default adds an s) add this code and get rid of the extra 's' on page after superuser login  localhost:8000/admin 
    class Meta:
        verbose_name_plural = "Posts" 
        #can change app name to Blog instead of Posts