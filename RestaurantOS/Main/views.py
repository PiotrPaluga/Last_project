from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from .models import Restaurant, Hours, Tables, HOUR_CHOICES, Reservation
from .forms import ReservationForm, LoginForm, RegisterForm, ModifyRestaurantForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class MainView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all().order_by('id')
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
            # pobieranie danych z formularza
            name = form.cleaned_data['name']
            participants = form.cleaned_data['participants']
            date = form.cleaned_data['date']
            start_hour_num = form.cleaned_data['start_hour']
            duration = form.cleaned_data['duration']
            # przetwarzanie godziny z liczby na czas do wywietlenia na stronie
            start_hour = HOUR_CHOICES[int(start_hour_num) - 1][1]
            end_hour_num = int(start_hour_num) + int(duration[0])
            end_hour = HOUR_CHOICES[int(end_hour_num) - 1][1]
            # szukanie wolnego stolika
            reservated_tables = Tables.objects.filter(
                restaurant_id=restaurant_id,
                reservation__start_hour__gte=start_hour_num,
                reservation__end_hour__lte=end_hour_num
            )
            free_tables = Tables.objects.filter(restaurant_id=restaurant_id, max_cap__gte=participants,
                                                min_cap__lte=participants).exclude(id__in=reservated_tables)
            if free_tables:
                table = free_tables[0]
                new_res = Reservation(restaurant_id=restaurant_id, guest=name, table=table, date=date,
                                      participants=participants, start_hour=start_hour_num, end_hour=end_hour_num)
                new_res.save()
                return render(request, 'reservation-view.html', {'restaurant': restaurant,
                                                                 'name': name, 'participants': participants,
                                                                 'date': date,
                                                                 'start_hour': start_hour, 'end_hour': end_hour})
            else:
                return render(request, 'reservation-view.html',
                              {'restaurant': restaurant, 'err': "Brak dostepnych stolikow na dana godzine."})
    else:
        if request.user.is_authenticated:
            name = request.user.first_name + " " + request.user.last_name
            form = ReservationForm(initial={'name': name})
            form.fields['name'].widget.attrs['readonly'] = True
            form.fields['start_hour'].choices = HOUR_CHOICES[10:40]
            return render(request, 'reservation-view.html', {'form': form, 'restaurant': restaurant})
        form = ReservationForm()
        form.fields['start_hour'].choices = HOUR_CHOICES[10:40]
        return render(request, 'reservation-view.html', {'form': form, 'restaurant': restaurant})


class SupportView(View):
    def get(self, request):
        return render(request, "support.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form = LoginForm()
                err = "Bledny login lub haslo!"
                return render(request, "login.html", {'form': form, 'err': err})
    else:
        form = LoginForm()
        return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                            last_name=lastname)
            msg = "Uzytkownik utworzony, mozesz sie teraz zalogowac!"
            return render(request, "register.html", {'err': msg})
        else:
            form = RegisterForm()
            err = "Podano niewlasciwe dane, sprobuj jeszcze raz!"
            return render(request, "register.html", {'form': form, 'err': err})

    else:
        form = RegisterForm()
        return render(request, "register.html", {'form': form})


def add_restaurant(request):
    if request.method == 'POST':
        form = ModifyRestaurantForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone_num = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            new_res = Restaurant(name=name, address=address, phone_number=phone_num, email=email)
            new_res.save()
            msg = "Twoja restauracja została dodana!"
            return render(request, "edit-restaurant.html", {'err': msg})

    else:
        form = ModifyRestaurantForm()
        return render(request, "edit-restaurant.html", {'form': form, 'button': "Dodaj"})


def edit_restaurant(request, restaurant_id):
    res = Restaurant.objects.get(id=restaurant_id)
    if request.method == 'POST':
        form = ModifyRestaurantForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone_num = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            res.name = name
            res.address = address
            res.phone_number = phone_num
            res.email = email
            res.save()
            msg = "Zmiany zostały zapisane!"
            return render(request, "edit-restaurant.html", {'err': msg})

    else:
        form = ModifyRestaurantForm(initial={'name': res.name, 'address': res.address, 'phone_number': res.phone_number,
                                             'email': res.email})
        return render(request, "edit-restaurant.html", {'form': form, 'button': "Edytuj"})


class EditList(View):
    def get(self, request):
        restaurants = Restaurant.objects.all().order_by('id')
        return render(request, 'restaurants.html', {'restaurants': restaurants, 'edit': 'edit'})

