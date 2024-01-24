from django.contrib import admin
from .models import CollaborativeProject

class CollaborativeProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'id') 
    search_fields = ('title', 'user__username')

admin.site.register(CollaborativeProject, CollaborativeProjectAdmin)
