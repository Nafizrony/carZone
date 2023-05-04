from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f'<img src="{object.car_photo.url}" width="60" style="border-radius:8px" >')
    list_display = ('vin','car_title','thumbnail','model','color','year','engine','is_featured')
    list_display_links = ('vin','car_title','thumbnail',)
    search_fields = ('car_title','model','body_style','engine')
    list_filter = ('city','model','engine','fuel_type')
    list_editable = ('is_featured',)


admin.site.register(Cars,CarAdmin)
admin.site.register(Car_Feature)
