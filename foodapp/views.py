from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from foodapp.models import Restaurant
from foodapp.forms import ReviewForm

# Create your views here.
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'foodapp/restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    return render(request, 'foodapp/restaurant_detail.html', {'restaurant': restaurant})

def restaurant_types(request, tag):
    restaurants = Restaurant.objects.filter(tag=tag)
    return render(request, 'foodapp/restaurant-types.html', {'restaurants': restaurants})

def add_review(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.save()
            return HttpResponseRedirect(reverse('foodapp:restaurant_detail',args = (restaurant.slug,)))
    else:
        form = ReviewForm()
    return render(request, 'foodapp/add_review.html', {'form': form})
