from django.contrib import admin
from .models import Restaurant, Tables, Reservation, Hours


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "address")


@admin.register(Tables)
class TablesAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'min_cap', 'max_cap')


@admin.register(Hours)
class HoursAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'day', 'open_hour', 'close_hour')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('guest', 'restaurant', 'date')
