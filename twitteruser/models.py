from django.db import models
from django.contrib.auth.models import AbstractUser

class TwitterUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    display_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40,
        blank=True, unique=True)
    following = models.ManyToManyField('self', blank=True, symmetrical=False)
    tweets = models.IntegerField(blank=True,
        default=0)
    
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['display_name', 'email']

    def __str__(self):
        return self.username