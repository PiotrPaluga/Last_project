from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from .models import Restaurant, Hours, Tables, HOUR_CHOICES, Reservation
from .forms import ReservationForm, LoginForm, RegisterForm, ModifyRestaurantForm, TableEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin


def is_superuser(user):
    return user.is_superuser


class MainView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all().order_by('id')
        return render(request, "restaurants.html", {'restaurants': restaurants})


class RestaurantView(View):
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        hours = Hours.objects.filter(restaurant_id=restaurant_id)
        true_hours = []
        for hour in hours:
            true_hours.append(HOUR_CHOICES[int(hour.open_hour)][1])
            true_hours.append(HOUR_CHOICES[int(hour.close_hour)][1])
        return render(request, "restaurant-view.html",
                      {'restaurant': restaurant, 'hours': true_hours})


@login_required
def reservation_view(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    active_user = request.user
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # pobieranie danych z formularza
            participants = form.cleaned_data['participants']
            date = form.cleaned_data['date']
            start_hour_num = form.cleaned_data['start_hour']
            duration = form.cleaned_data['duration']

            # przetwarzanie godziny z liczby na czas do wywietlenia na stronie
            start_hour = HOUR_CHOICES[int(start_hour_num)][1]
            end_hour_num = int(start_hour_num) + int(duration[0])
            end_hour = HOUR_CHOICES[int(end_hour_num)][1]

            # szukanie wolnego stolika
            reservated_tables = Tables.objects.filter(
                restaurant_id=restaurant_id,
                reservation__start_hour__gte=start_hour_num,
                reservation__end_hour__lte=end_hour_num,
                reservation__date=date
            )
            free_tables = Tables.objects.filter(restaurant_id=restaurant_id, max_cap__gte=participants,
                                                min_cap__lte=participants).exclude(id__in=reservated_tables)
            if free_tables:
                table = free_tables[0]
                new_res = Reservation(restaurant_id=restaurant_id, guest=active_user, table=table, date=date,
                                      participants=participants, start_hour=start_hour_num, end_hour=end_hour_num)
                new_res.save()
                return render(request, 'reservation-view.html', {'restaurant': restaurant,
                                                                 'participants': participants,
                                                                 'date': date,
                                                                 'start_hour': start_hour, 'end_hour': end_hour})
            else:
                return render(request, 'reservation-view.html',
                              {'restaurant': restaurant, 'err': "Brak dostepnych stolikow na dana godzine."})
    else:
        form = ReservationForm()
        form.fields['start_hour'].choices = HOUR_CHOICES[10:48]
        return render(request, 'reservation-view.html', {'form': form, 'restaurant': restaurant,
                                                         'user': active_user})


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


@user_passes_test(is_superuser)
def add_restaurant(request):
    if request.method == 'POST':
        form = ModifyRestaurantForm(request.POST)
        if form.is_valid():
            # Dane restauracji:-----------------------------------------
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone_num = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            # Godziny otwarcia:-----------------------------------------
            pon_czw_start = form.cleaned_data['pon_czw_start']
            pon_czw_end = form.cleaned_data['pon_czw_end']
            pt_sob_start = form.cleaned_data['pt_sob_start']
            pt_sob_end = form.cleaned_data['pt_sob_end']
            nd_start = form.cleaned_data['nd_start']
            nd_end = form.cleaned_data['nd_end']
            # Tworzenie obiektów i zapisywanie ich w bazie:-------------
            new_res = Restaurant(name=name, address=address, phone_number=phone_num, email=email)
            new_res.save()
            new_res_pon_czw = Hours(restaurant_id=new_res.id, day=1, open_hour=pon_czw_start, close_hour=pon_czw_end)
            new_res_pon_czw.save()
            new_res_pt_sob = Hours(restaurant_id=new_res.id, day=2, open_hour=pt_sob_start, close_hour=pt_sob_end)
            new_res_pt_sob.save()
            new_res_nd = Hours(restaurant_id=new_res.id, day=3, open_hour=nd_start, close_hour=nd_end)
            new_res_nd.save()

            msg = "Twoja restauracja została dodana!"
            return render(request, "edit-restaurant.html", {'err': msg})

    else:
        form = ModifyRestaurantForm()
        return render(request, "edit-restaurant.html", {'form': form, 'button': "Dodaj"})


@user_passes_test(is_superuser)
def edit_restaurant(request, restaurant_id):
    res = Restaurant.objects.get(id=restaurant_id)
    res_pon_czw = Hours.objects.get(restaurant_id=restaurant_id, day=1)
    res_pt_sob = Hours.objects.get(restaurant_id=restaurant_id, day=2)
    res_nd = Hours.objects.get(restaurant_id=restaurant_id, day=3)
    if request.method == 'POST':
        form = ModifyRestaurantForm(request.POST)
        if form.is_valid():
            # Dane restauracji:------------------------------------
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone_num = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            # Godziny otwarcia: -----------------------------------
            pon_czw_start = form.cleaned_data['pon_czw_start']
            pon_czw_end = form.cleaned_data['pon_czw_end']
            pt_sob_start = form.cleaned_data['pt_sob_start']
            pt_sob_end = form.cleaned_data['pt_sob_end']
            nd_start = form.cleaned_data['nd_start']
            nd_end = form.cleaned_data['nd_end']
            # Edycja bazy danych:----------------------------------
            res.name = name
            res.address = address
            res.phone_number = phone_num
            res.email = email
            res.save()
            res_pon_czw.open_hour = pon_czw_start
            res_pon_czw.close_hour = pon_czw_end
            res_pon_czw.save()
            res_pt_sob.open_hour = pt_sob_start
            res_pt_sob.close_hour = pt_sob_end
            res_pt_sob.save()
            res_nd.open_hour = nd_start
            res_nd.close_hour = nd_end
            res_nd.save()
            msg = "Zmiany zostały zapisane!"
            return render(request, "edit-restaurant.html", {'err': msg})

    else:
        initials = {
            'name': res.name,
            'address': res.address,
            'phone_number': res.phone_number,
            'email': res.email,
            'pon_czw_start': res_pon_czw.open_hour,
            'pon_czw_end': res_pon_czw.close_hour,
            'pt_sob_start': res_pt_sob.open_hour,
            'pt_sob_end': res_pt_sob.close_hour,
            'nd_start': res_nd.open_hour,
            'nd_end': res_nd.close_hour
        }
        form = ModifyRestaurantForm(initial=initials)
        return render(request, "edit-restaurant.html", {'form': form, 'button': "Edytuj"})


@user_passes_test(is_superuser)
def delete_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    restaurant.delete()
    return redirect('edit-list')


class EditList(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        restaurants = Restaurant.objects.all().order_by('id')
        return render(request, 'restaurants.html', {'restaurants': restaurants, 'edit': 'edit'})


class TablesView(UserPassesTestMixin, View):

    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        tables = Tables.objects.filter(restaurant_id=restaurant_id)
        return render(request, 'tables-view.html', {'tables': tables, 'restaurant': restaurant})

    def test_func(self):
        return self.request.user.is_superuser


@user_passes_test(is_superuser)
def table_edit(request, restaurant_id, table_id):
    table = Tables.objects.get(id=table_id, restaurant_id=restaurant_id)
    if request.method == 'POST':
        form = TableEditForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            min_cap = form.cleaned_data['min_cap']
            max_cap = form.cleaned_data['max_cap']
            table.name = name
            table.min_cap = min_cap
            table.max_cap = max_cap
            table.save()
            return redirect(f'/restaurant/{restaurant_id}/tables/')

    else:
        form = TableEditForm(initial={'name': table.name, 'min_cap': table.min_cap, 'max_cap': table.max_cap})
        return render(request, 'edit-table.html', {'form': form, 'button': "Edytuj"})


@user_passes_test(is_superuser)
def table_add(request, restaurant_id):
    if request.method == 'POST':
        form = TableEditForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            min_cap = form.cleaned_data['min_cap']
            max_cap = form.cleaned_data['max_cap']
            new_table = Tables(restaurant_id=restaurant_id, name=name, min_cap=min_cap, max_cap=max_cap)
            new_table.save()
            return redirect(f'/restaurant/{restaurant_id}/tables/')

    else:
        form = TableEditForm()
        return render(request, 'edit-table.html', {'form': form, 'button': "Dodaj"})


@user_passes_test(is_superuser)
def table_delete(request, restaurant_id, table_id):
    table = Tables.objects.get(id=table_id, restaurant_id=restaurant_id)
    table.delete()
    return redirect(f'/restaurant/{restaurant_id}/tables/')


@login_required
def user_panel(request):
    active_user = request.user
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['firstname']
            last = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            active_user.first_name = first
            active_user.last_name = last
            active_user.email = email
            active_user.save()
            return redirect('user-panel')
        return redirect('user-panel')

    else:
        reservations = Reservation.objects.filter(guest=active_user)
        initials = {
            'firstname': active_user.first_name,
            'lastname': active_user.last_name,
            'email': active_user.email
        }
        form = RegisterForm(initial=initials)
        return render(request, 'user-view.html', {'user': active_user, 'form': form,
                                                  'reservations': reservations, 'hours': HOUR_CHOICES})


@login_required
def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.delete()
    return redirect('user-panel')
