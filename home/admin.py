from django.contrib import admin
from .models import Artwork, Comment, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')

admin.site.register(Artwork)
admin.site.register(Comment)
admin.site.register(UserProfile, UserProfileAdmin)

