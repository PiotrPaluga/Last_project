from django.views import View
from django.shortcuts import render
from .models import Restaurant, Reservation, Hours, Guest, Tables

class MainView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        return render(request, "restaurants.html", {'restaurants': restaurants})

class RestaurantView(View):
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        return render(request, "restaurant-view.html", {'restaurant': restaurant})
