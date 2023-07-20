from django.contrib import admin

from django.contrib import admin
from .models import Note
# Register your models here.

class NoteManger(admin.ModelAdmin):
    list_display = ['title', 'content', 'create_time', 'response']
    list_display_links = ['title']
    search_fields = ['title']


admin.site.register(Note, NoteManger)
admin.site.site_header = '意见反馈系统后台'



# Register your models here.
