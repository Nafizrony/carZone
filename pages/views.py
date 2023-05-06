from django.shortcuts import render
from .models import Team
from cars.models import Cars

# Create your views here.

def home(request):
    team_members = Team.objects.all()
    features_cars = Cars.objects.filter(is_featured=True)
    new_cars = Cars.objects.order_by('-created')
    search_model = Cars.objects.values_list('model',flat=True).distinct()
    search_city = Cars.objects.values_list('city',flat=True).distinct()
    search_year = Cars.objects.values_list('year',flat=True).distinct()
    search_body_style = Cars.objects.values_list('body_style',flat=True).distinct()

    if request.GET.get('min_price'):
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if max_price:
          cars =   Cars.objects.filter(car_price__gte=min_price,car_price__lte=max_price)


    context = {'team_members':team_members,'features_cars':features_cars,
               'latest_cars':new_cars,'search_model':search_model,'search_city':search_city,
               'search_year':search_year,'search_body_style':search_body_style}
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

