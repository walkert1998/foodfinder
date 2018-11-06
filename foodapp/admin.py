from django.contrib import admin
from .models import Restaurant
from foodapp.models import Review

# Register your models here.

class ReviewInLine(admin.StackedInline):
    model = Review
    fields = ('name','rating','review_text')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ReviewInLine]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review)
