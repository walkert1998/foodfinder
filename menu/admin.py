# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from adminsortable.admin import StackedInline
from django.contrib import admin
from menu.models import MenuItem
from menu.models import Menu
# Register your models here.

class MenuItemInline(StackedInline):
    model = MenuItem
    fields = ('item_name','price','notes')


class MenuItemAdmin():
    model = MenuItem
    fields = ('item_name','price','notes')

class MenuAdmin():
    inlines = [MenuItemInline]

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
