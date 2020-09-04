from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser


class Notification(models.Model):
    tweet_message = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    notification_view = models.BooleanField(default=False)

    def __str__(self):
        return self.tweet_message.body