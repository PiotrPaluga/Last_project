from django import forms
from .models import HOUR_CHOICES


class ReservationForm(forms.Form):
    name = forms.CharField(label='Imie i nazwisko', max_length=64)
    participants = forms.IntegerField(label='Ilosc osob')
    date = forms.DateField(label='Data (DD/MM/YYYY)', input_formats=['%d/%m/%Y', '%d.%m.%Y', '%d-%m-%Y'])
    start_hour = forms.ChoiceField(label='Godzina rozpoczecia', choices=HOUR_CHOICES)
    duration = forms.ChoiceField(label='Czas trwania',
                                 choices=((1, "0:30"), (2, "1:00"), (3, "1:30"), (4, "2:00"), (5, "2:30"), (6, "3:00")))


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=64)
    password = forms.CharField(label='Haslo', max_length=64, widget=forms.PasswordInput)


class RegisterForm(LoginForm):
    firstname = forms.CharField(label='Imie', max_length=64)
    lastname = forms.CharField(label='Nazwisko', max_length=64)
    email = forms.EmailField(label='E-mail', max_length=64)


class ModifyRestaurantForm(forms.Form):
    name = forms.CharField(label='Nazwa restauracji', max_length=64)
    address = forms.CharField(label='Adres restauracji', max_length=64)
    phone_number = forms.CharField(label='Numer telefonu', max_length=16)
    email = forms.EmailField(label='E-mail', max_length=64)
