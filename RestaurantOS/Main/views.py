from django.views import View
from django.shortcuts import render
from .models import Restaurant, Reservation, Hours, Guest, Tables

class MainView(View):
    def get(self, request):
        return render(request, "base.html")
