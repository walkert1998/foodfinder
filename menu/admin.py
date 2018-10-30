# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from adminsortable.admin import StackedInline
from django.contrib import admin
from menu.models import MenuItem
from menu.models import Menu
# Register your models here.

class MenuItemInline(admin.StackedInline):
    model = MenuItem
    list_display = ['item_name','price']
    fields = ('item_name','price','notes')


class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = ['item_name', 'price']
    fields = ('item_name','price','notes')

class MenuAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [MenuItemInline]

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
