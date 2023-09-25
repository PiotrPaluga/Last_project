from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    email = models.CharField(max_length=64)


class Hours(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.CharField(max_length=32)
    open_hour = models.TimeField()
    close_hour = models.TimeField()


class Tables(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_nr = models.CharField(max_length=64)
    min_cap = models.IntegerField
    max_cap = models.IntegerField


class Guest(models.Model):
    guest_name = models.CharField(max_length=64)
    guest_phone = models.CharField(max_length=16)


class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    date = models.DateField
    participants = models.IntegerField
    start = models.TimeField
    end = models.TimeField
