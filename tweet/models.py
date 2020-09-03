from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    
    body = models.TextField(max_length=140)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    time_created = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.body