from django.contrib import admin
from .models import Url

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['orginal_url', 'short_link', 'created']
    list_per_page = 20
    date_hierarchy = 'created'