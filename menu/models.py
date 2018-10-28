from __future__ import unicode_literals

from django.db import models
from cms.models.pluginmodel import CMSPlugin

# Create your models here.
class Menu(CMSPlugin):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu)
    item_name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.item_name

    def __unicode__(self):
        return self.item_name
