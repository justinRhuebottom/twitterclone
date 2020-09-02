from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUser

@admin.register(TwitterUser)
class TwiterAdmin(admin.ModelAdmin):
    readonly_fields = ['password']