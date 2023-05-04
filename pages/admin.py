from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f'<img src="{object.profile_pic.url}" width="40" style="border-radius:20px" >')
    thumbnail.short_description = "Photo"
    list_display = ('id','thumbnail','first_name','designation','created')
    list_display_links = ('id','first_name','thumbnail')
    search_fields = ('first_name','designation','last_name')
    list_filter = ('designation',)



admin.site.register(Team,TeamAdmin)
