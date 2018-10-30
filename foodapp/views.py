from django.shortcuts import render
from django.shortcuts import get_object_or_404
from foodapp.models import Restaurant

# Create your views here.
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'foodapp/restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'foodapp/restaurant_detail.html', {'restaurant': restaurant})
