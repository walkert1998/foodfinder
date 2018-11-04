from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from foodapp.models import Restaurant
from foodapp.forms import ReviewForm

# Create your views here.
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'foodapp/restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'foodapp/restaurant_detail.html', {'restaurant': restaurant})

def add_review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = ReviewForm()
    return render(request, 'foodapp/add_review.html', {'form': form})
