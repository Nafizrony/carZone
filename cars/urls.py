from django.urls import path
from . import views

urlpatterns = [
    path('',views.cars,name='cars'),
    path('search/',views.search,name='search'),
    path('<str:pk>/',views.single_car,name='single_car'),
]
