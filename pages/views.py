from django.shortcuts import render
from .models import Team
from cars.models import Cars
# Create your views here.

def home(request):
    team_members = Team.objects.all()
    features_cars = Cars.objects.filter(is_featured=True)
    new_cars = Cars.objects.order_by('-created')
    context = {'team_members':team_members,'features_cars':features_cars,'latest_cars':new_cars}
    return render(request,'pages/home.html',context)

def about(request):
    context = {}
    return render(request,'pages/about.html',context)

def services(request):
    context = {}
    return render(request,'pages/services.html',context)

def contact(request):
    context = {}
    return render(request,'pages/contact.html',context)
