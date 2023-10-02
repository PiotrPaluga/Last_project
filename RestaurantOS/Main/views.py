from django.views import View
from django.shortcuts import render, HttpResponse
from .models import Restaurant, Reservation, Hours, Tables
from .forms import ReservationForm


class MainView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        return render(request, "restaurants.html", {'restaurants': restaurants})


class RestaurantView(View):
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        return render(request, "restaurant-view.html", {'restaurant': restaurant})


def reservation_view(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            participants = form.cleaned_data['participants']
            date = form.cleaned_data['date']
            hour = form.cleaned_data['hour']
            new_res = Reservation(restaurant_id=restaurant_id, guest=name, table_id=1, date=date,
                                  participants=participants, start=hour)
            new_res.save()
            return render(request, 'reservation-view.html', {'restaurant': restaurant,
                                                             'name': name, 'participants': participants, 'date': date,
                                                             'hour': hour})
    else:
        form = ReservationForm()
    return render(request, 'reservation-view.html', {'form': form, 'restaurant': restaurant})


class SupportView(View):
    def get(self, request):
        return render(request, "support.html")
