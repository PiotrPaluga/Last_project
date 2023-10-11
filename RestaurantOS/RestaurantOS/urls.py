"""
URL configuration for RestaurantOS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Main.views import MainView, RestaurantView, SupportView, reservation_view, login_view, logout_view, register_view, add_restaurant, edit_restaurant, EditList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='home'),
    path('restaurant/<int:restaurant_id>/', RestaurantView.as_view()),
    path('support/', SupportView.as_view(), name="support"),
    path('restaurant/<int:restaurant_id>/reservation', reservation_view),
    path('login/', login_view, name='login-view'),
    path('logout/', logout_view, name='logout-view'),
    path('register/', register_view, name='register-view'),
    path('restaurant/add/', add_restaurant, name='add-restaurant'),
    path('edit/', EditList.as_view(), name='edit-list'),
    path('restaurant/<int:restaurant_id>/edit/', edit_restaurant, name='edit-restaurant'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
