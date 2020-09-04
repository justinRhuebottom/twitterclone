from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser

@login_required
def notification_view(request):
    unseen_messages = Notification.objects.filter(user=request.user).filter(notification_view=False)
    
    # filter each mention 
    # in all the tweets
    # for unseen notifications 
    tweets = Tweet.objects.filter(id__in=[x.tweet_message.id for x in unseen_messages]).order_by("-time_created")
    for unseen_message in unseen_messages:
        unseen_message.notification_view = True
        unseen_message.save()
    return render(request, "notification.html", {'tweets': tweets})