from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.

def cars(request):
    cars = Cars.objects.all()
    context = {'cars':cars}
    return render(request,'cars/cars.html',context)

def single_car(request,pk):
    car_info = get_object_or_404(Cars, id=pk)
    # car_info = Cars.objects.get(id=pk)
    context = {'car_info':car_info}
    return render(request,'cars/car_details.html',context)