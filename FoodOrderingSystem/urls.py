"""
URL configuration for FoodOrderingSystem project.

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from Products.views import *
# from . import views
import uuid

urlpatterns = [
    path('', home, name="Home"),
    path('home/', home_2, name="Home"),
    path('about/', aboutPage, name="aboutPage"),
    path('menue/', menuePage, name="menuePage"),
    path('register/', register_page, name="register_page"),
    path('login_page/', login_page, name="login_page"),
    path('logout_page/', logout_page, name="logout_page"),
    path('reservation/', reservationPage, name="reservationPage"),
    path('user/', userPage, name="userPage"),
    path('addMenue/', addMenue, name="addMenuePage"),
    #___________________________________________CART____________________________________
    path('add/<uuid:id>/', cart_add, name='cart_add'),
    path('item_clear/<uuid:id>/', item_clear, name='item_clear'),
    path('item_increment/<uuid:id>/', item_increment, name='item_increment'),
    path('item_decrement/<uuid:id>/', item_decrement, name='item_decrement'),
    path('cart_clear/', cart_clear, name='cart_clear'),
    path('cart-detail/', cart_detail, name='cart_detail'),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
