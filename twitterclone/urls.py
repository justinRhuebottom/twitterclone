"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import index_view, login_view, logout_view, register_view
from tweet.views import add_tweet_view, tweet_view, author_view, follow_view
from notification.views import notification_view

urlpatterns = [
    path('', index_view, name="homepage"),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('addTweet/', add_tweet_view),
    path('tweet/<int:tweet_id>/', tweet_view),
    path('author/<str:author_name>/', author_view),
    path('follow/<str:author_name>/', follow_view),
    path('notification/', notification_view),
    path('admin/', admin.site.urls),
]
