from django import forms
from .models import HOUR_CHOICES


class ReservationForm(forms.Form):
    participants = forms.IntegerField(label='Ilosc osob')
    date = forms.DateField(label='Data (DD/MM/YYYY)', input_formats=['%d/%m/%Y', '%d.%m.%Y', '%d-%m-%Y'])
    start_hour = forms.ChoiceField(label='Godzina rozpoczecia', choices=HOUR_CHOICES)
    duration = forms.ChoiceField(label='Czas trwania',
                                 choices=('00:30', '01:00', '01:30', '02:00', '02:30', '03:00'))


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
    pon_czw_start = forms.ChoiceField(label='Godziny otwarcia Pn-Czw', choices=HOUR_CHOICES)
    pon_czw_end = forms.ChoiceField(choices=HOUR_CHOICES)
    pt_sob_start = forms.ChoiceField(label='Godziny otwarcia Pt-Sob', choices=HOUR_CHOICES)
    pt_sob_end = forms.ChoiceField(choices=HOUR_CHOICES)
    nd_start = forms.ChoiceField(label='Godziny otwarcia Nd', choices=HOUR_CHOICES)
    nd_end = forms.ChoiceField(choices=HOUR_CHOICES)


class TableEditForm(forms.Form):
    name = forms.CharField(label='Nazwa/Numer stolika', max_length=32)
    min_cap = forms.IntegerField(min_value=1)
    max_cap = forms.IntegerField(min_value=1)
