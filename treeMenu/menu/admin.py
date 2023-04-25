from django.contrib import admin
from .models import *


class MenuAdmin(admin.ModelAdmin):
    fields = ['name']


class ListAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'menu']
    list_display = ['name', 'description', 'menu']


admin.site.register(Menu, MenuAdmin)
admin.site.register(List, ListAdmin)
