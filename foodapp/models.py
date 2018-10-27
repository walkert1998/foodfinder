from django.db import models
from menu.models import Menu

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True, null=True)
    menu_already_online = models.BooleanField(blank=True, default=False)
    twitter_link = models.CharField(max_length=200, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    instagram_link = models.CharField(max_length=200, blank=True, null=True)

    menu = models.ForeignKey(Menu)

    def __str__(self):
        return self.name
