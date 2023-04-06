from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:50px" />'.format(object.car_photo.url))
    
    thumbnail.short_description='car images'
    list_display=('id','thumbnail','care_title','city','color','model','year','body_style','fuel_type','is_featured')
    list_display_links=('id','thumbnail','care_title',)
    last_editable=('is_featured')
    search_fields=('id','care_title','city','model','body_style','fuel_type')
    last_filter=('city','model','body_style','fuel_type')

admin.site.register(Car,CarAdmin)