from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('car_details/<int:id>/', views.CarDetailsView, name="car_details"),
    path('buy/<int:id>/', views.update_quantity, name="buy_car"),
]
