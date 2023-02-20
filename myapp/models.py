from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notifications(models.Model):
    title=models.CharField(max_length=400,blank=True)
    poster=models.ImageField(upload_to="images",default="")
    description=models.CharField(max_length=400,blank=True)
    content=models.CharField(max_length=400,blank=True)
    date_sent=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title


class News(models.Model):
    author=models.CharField(max_length=400,blank=True)
    title=models.CharField(max_length=400,blank=True)
    content=models.CharField(max_length=4000,blank=True)
    description=models.CharField(max_length=4000,blank=True)
    urlToImage=models.CharField(max_length=400,blank=True)
    source=models.CharField(max_length=400,blank=True)
    publishedAt=models.DateTimeField(auto_now_add=True,blank=True)
    url=models.CharField(max_length=400,blank=True)
    category=models.CharField(max_length=400,blank=True)

    def __str__(self):
        return self.title


    








