from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    email = models.CharField(max_length=64)


class Hours(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.CharField(max_length=32)
    open_hour = models.TimeField(null=True)
    close_hour = models.TimeField(null=True)


class Tables(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_nr = models.CharField(max_length=64)
    min_cap = models.IntegerField(null=True)
    max_cap = models.IntegerField(null=True)


class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    guest = models.CharField(max_length=64)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    participants = models.IntegerField(null=True)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)
