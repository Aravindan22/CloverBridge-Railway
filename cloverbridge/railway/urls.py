

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.seat_finder, name='seat_finder'),
]
