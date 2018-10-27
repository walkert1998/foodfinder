# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cms.models import CMSPlugin

# Create your models here.
def Menu(CMSPlugin):
    name = models.CharField(max_length=100, blank=True, null=True)

def MenuItem():
    menu = models.ForeignKey(Menu)
    item_name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.item_name
