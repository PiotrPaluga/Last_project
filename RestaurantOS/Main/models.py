from django.db import models
from django.contrib.auth.models import User

HOUR_CHOICES = ('00:00'  '00:30',
                '01:00'  '01:30',
                '02:00'  '02:30',
                '03:00'  '03:30',
                '04:00'  '04:30',
                '05:00', '05:30',
                '06:00', '06:30',
                '07:00', '07:30',
                '08:00', '08:30',
                '09:00', '09:30',
                '10:00', '10:30',
                '11:00', '11:30',
                '12:00', '12:30',
                '13:00', '13:30',
                '14:00', '14:30',
                '15:00', '15:30',
                '16:00', '16:30',
                '17:00', '17:30',
                '18:00', '18:30',
                '19:00', '19:30',
                '20:00', '20:30',
                '21:00', '21:30',
                '22:00', '22:30',
                '23:00', '23:30',
                )


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    email = models.CharField(max_length=64)


class Hours(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.IntegerField()
    open_hour = models.IntegerField()
    close_hour = models.IntegerField()


class Tables(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)
    min_cap = models.IntegerField()
    max_cap = models.IntegerField()


class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    date = models.DateField()
    participants = models.IntegerField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
