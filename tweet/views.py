from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import AddTweetForm
from twitteruser.models import TwitterUser

@login_required()
def add_tweet_view(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body=data.get('body'),
                author=request.user
            )
            user = TwitterUser.objects.get(id=request.user.id)
            user.tweets += 1
            user.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddTweetForm()
    return render(request, "add_tweet.html", {"form": form})

def tweet_view(request, tweet_id):
    return render(request, 'tweet.html', {"tweet": Tweet.objects.filter(id=tweet_id).first()})

def author_view(request, author_name):
    author_id = TwitterUser.objects.get(username=author_name).id
    author = TwitterUser.objects.filter(id=author_id).first()
    tweets = Tweet.objects.filter(author=author)
    following = list(request.user.following.all())
    follower = TwitterUser.objects.get(username=author_name)
    if follower in following:
        button_status = 'Unfollow'
    else:
        button_status = 'Follow'
    return render(request, 'author.html', {"author": author, "tweets": tweets, "button_status": button_status})

@login_required()
def follow_view(request, author_name):
    following = list(request.user.following.all())
    follower = TwitterUser.objects.get(username=author_name)
    if follower in following:
        request.user.following.remove(follower)
        request.user.save()
    else:
        request.user.following.add(follower)
        request.user.save()
    return HttpResponseRedirect(reverse("homepage"))