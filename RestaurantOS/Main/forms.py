from django import forms


class ReservationForm(forms.Form):
    name = forms.CharField(label='Imie i nazwisko', max_length=64)
    participants = forms.IntegerField(label='Ilosc osob')
    date = forms.DateField(label='Data (DD/MM/YYYY)', input_formats=['%d/%m/%Y', '%d.%m.%Y', '%d-%m-%Y'])
    hour = forms.TimeField(label='Godzina reserwacji (HH:MM)', input_formats=['%H:%M'])
