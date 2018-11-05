from django.contrib import admin
from .models import Restaurant
from foodapp.models import Tag
from foodapp.models import Review

# Register your models here.
class TagInline(admin.StackedInline):
    model = Tag
    fields = ('tag',)

class ReviewInLine(admin.StackedInline):
    model = Review
    fields = ('customer_name','rating','review_text')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [TagInline, ReviewInLine]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review)
