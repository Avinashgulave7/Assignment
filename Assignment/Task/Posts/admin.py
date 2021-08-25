from django.contrib import admin
from .models import POST

@admin.register(POST)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','text','created_at','updated_at']
