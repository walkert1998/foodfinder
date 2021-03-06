from django.db import models
from django.utils import timezone

# Create your models here.

TAGS = [
    ('cafe', 'Cafe'),
    ('pizza', 'Pizza'),
    ('pub', 'Pub'),
    ('global', 'Global'),
    ('bistro', 'Bistro'),
]
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    menu_link = models.CharField(max_length=200, blank=True, default=False)
    lowest_price = models.IntegerField(null=True, blank=True)
    highest_price = models.IntegerField(null=True, blank=True)
    delivery_services = models.BooleanField(blank=True, default=False)
    student_discounts = models.BooleanField(blank=True, default=False)
    free_wifi = models.BooleanField(blank=True, default=False)
    gluten_free_options = models.BooleanField(blank=True, default=False)
    serves_alcohol = models.BooleanField(blank=True, default=False)
    vegetarian_options = models.BooleanField(blank=True, default=False)
    vegan_options = models.BooleanField(blank=True, default=False)
    twitter_link = models.CharField(max_length=200, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    instagram_link = models.CharField(max_length=200, blank=True, null=True)
    monday_hours = models.CharField(max_length=200, blank=True, null=True)
    tuesday_hours = models.CharField(max_length=200, blank=True, null=True)
    wednesday_hours = models.CharField(max_length=200, blank=True, null=True)
    thursday_hours = models.CharField(max_length=200, blank=True, null=True)
    friday_hours = models.CharField(max_length=200, blank=True, null=True)
    saturday_hours = models.CharField(max_length=200, blank=True, null=True)
    sunday_hours = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=200, choices=TAGS, default='cafe')
    slug = models.SlugField(max_length=200, null=True, unique=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField()
    review_text = models.TextField(null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.review_text
