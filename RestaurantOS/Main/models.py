from django.db import models
from django.contrib.auth.models import User

HOUR_CHOICES = (
    (0, '00:00'), (1, '00:30'),
    (2, '01:00'), (3, '01:30'),
    (4, '02:00'), (5, '02:30'),
    (6, '03:00'), (7, '03:30'),
    (8, '04:00'), (9, '04:30'),
    (10, '05:00'), (11, '05:30'),
    (12, '06:00'), (13, '06:30'),
    (14, '07:00'), (15, '07:30'),
    (16, '08:00'), (17, '08:30'),
    (18, '09:00'), (19, '09:30'),
    (20, '10:00'), (21, '10:30'),
    (22, '11:00'), (23, '11:30'),
    (24, '12:00'), (25, '12:30'),
    (26, '13:00'), (27, '13:30'),
    (28, '14:00'), (29, '14:30'),
    (30, '15:00'), (31, '15:30'),
    (32, '16:00'), (33, '16:30'),
    (34, '17:00'), (35, '17:30'),
    (36, '18:00'), (37, '18:30'),
    (38, '19:00'), (39, '19:30'),
    (40, '20:00'), (41, '20:30'),
    (42, '21:00'), (43, '21:30'),
    (44, '22:00'), (45, '22:30'),
    (46, '23:00'), (47, '23:30'),
)


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    date = models.DateField()
    participants = models.IntegerField()
    start_hour = models.IntegerField()
    end_hour = models.IntegerField()

    def __str__(self):
        return self.guest.first_name
