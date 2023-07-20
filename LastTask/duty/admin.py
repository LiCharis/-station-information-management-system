from django.contrib import admin

# Register your models here.
from django.contrib import admin

from django.contrib import admin
from .models import Duty
# Register your models here.

class DutyManger(admin.ModelAdmin):
    list_display = ['create_time', 'flow', 'rate', 'condition', 'attendance', 'emergency', 'clear', 'response']
    list_display_links = ['create_time']
    search_fields = ['create_time']

admin.site.register(Duty, DutyManger)

# Register your models here.
