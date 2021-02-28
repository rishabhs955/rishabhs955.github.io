from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class likedislike(models.Model):
    atomic=False
    image = models.ImageField(upload_to='img/')
    like = models.ManyToManyField(User, related_name ='like')
    dislike = models.ManyToManyField(User, related_name ='dislike')

