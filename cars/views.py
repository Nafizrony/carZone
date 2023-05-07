from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q 

# Create your views here.



def cars(request):
    cars = Cars.objects.all()
    page = request.GET.get('page')
    result = 3
    paginator = Paginator(cars,result)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        cars = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        cars = paginator.page(page)

    city_search = Cars.objects.values_list('city',flat=True).distinct()
    year_search = Cars.objects.values_list('year',flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style',flat=True).distinct()
    transmission_search = Cars.objects.values_list('transmission',flat=True).distinct()


    if request.GET.get('model'):
        model = request.GET.get('model')
        if model:
            cars = Cars.objects.filter(model__iexact=model)

    if request.GET.get('city'):
        city = request.GET.get('city')
        if city:
            cars = Cars.objects.filter(city__iexact=city)

    if request.GET.get('year'):
        year = request.GET.get('year')
        if year:
            cars = Cars.objects.filter(year__iexact=year)

    if request.GET.get('body_style'):
        body_style = request.GET.get('body_style')
        if body_style:
            cars = Cars.objects.filter(body_style__iexact=body_style)
    # if request.GET.get('min_price'):
    #     min_price = request.GET.get('min_price')
    #     max_price = request.GET.get('max_price')
    #     if max_price:
    #         cars = Cars.objects.filter(car_price__gte=min_price,car_price__lte=max_price)
    context = {'cars':cars,'paginator':paginator,'page':page,
            'city_search':city_search,'year_search':year_search,
            'body_style_search':body_style_search,'transmission_search':transmission_search}
    return render(request,'cars/cars.html',context)

def single_car(request,pk):
    car_info = get_object_or_404(Cars, id=pk)
    # car_info = Cars.objects.get(id=pk)

    context = {'car_info':car_info,}
    return render(request,'cars/car_details.html',context)


def search(request):
    query_search = ''
    search_cars = ''
    if request.GET.get('query_search'):
        query_search = request.GET.get('query_search')
        state_search = Cars.objects.values_list('state',flat=True).distinct()
        if  query_search:
            search_cars = Cars.objects.distinct().filter(
                Q(car_title__icontains=query_search)|
                Q(city__icontains=query_search)|
                Q(state__iexact=state_search)|
                Q(features__name__icontains=query_search)|
                Q(color__icontains=query_search)|
                Q(model__icontains=query_search)|
                Q(description__icontains=query_search)|
                Q(body_style__icontains=query_search)|
                Q(engine__icontains=query_search)|
                Q(transmission__icontains=query_search)|
                Q(interior__icontains=query_search)    
            )
        
    condition_search = Cars.objects.values_list('condition',flat=True).distinct()
    year_search = Cars.objects.values_list('year',flat=True).distinct()
    city_search = Cars.objects.values_list('city',flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style',flat=True).distinct()
    model_search = Cars.objects.values_list('model',flat=True).distinct()
    transmission_search = Cars.objects.values_list('transmission',flat=True).distinct()
    if request.GET.get('model'):
        model = request.GET.get('model')
        if model:
            search_cars = Cars.objects.filter(model__iexact=model)

    if request.GET.get('city'):
        city = request.GET.get('city')
        if city:
            search_cars = Cars.objects.filter(city__iexact=city)

    if request.GET.get('year'):
        year = request.GET.get('year')
        if year:
            search_cars = Cars.objects.filter(year__iexact=year)

    if request.GET.get('body_style'):
        body_style = request.GET.get('body_style')
        if body_style:
            search_cars = Cars.objects.filter(body_style__iexact=body_style)
    
    if request.GET.get('condition'):
        condition = request.GET.get('condition')
        if condition:
            search_cars = Cars.objects.filter(condition__iexact=condition)

    if request.GET.get('transmission'):
        transmission = request.GET.get('transmission')
        if transmission:
            search_cars = Cars.objects.filter(transmission__iexact=transmission)

    # if request.GET.get('min_price'):
    #     min_price = request.GET.get('min_price')
    #     max_price = request.GET.get('max_price')
    #     if max_price:
    #         search_cars = Cars.objects.filter(car_price__gte=min_price,car_price__lte=max_price)

    context = {'search_cars':search_cars,'condition_search':condition_search,'year_search':year_search,
               'city_search':city_search,'body_style_search':body_style_search,
               'model_search':model_search,'transmission_search':transmission_search}
    return render(request,'cars/search.html',context)