from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.views import View
from authentication.forms import LoginForm, RegisterForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet

class indexView(View):
    def get(self, request):
        # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#in
        tweets = Tweet.objects.filter(
            author_id__in=request.user.following.all()) | Tweet.objects.filter(author=request.user)
        return render(request, "index.html", {"tweets": tweets.all().order_by('-time_created')})

class loginView(View):
    form_class = LoginForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, "login_form.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))

class registerView(View):
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, "register_form.html", {"form": form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get("username"),
                display_name=data.get("display_name"),
                email=data.get("email"), 
                password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    
class logoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("homepage"))