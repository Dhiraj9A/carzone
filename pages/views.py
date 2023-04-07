from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.order_by('-created_date')

    # search_fields=Car.objects.values('model','city','year','body_style')

    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style=Car.objects.values_list('body_style',flat=True).distinct()

    data={
        'teams':teams,
        'featured_car':featured_car,
        'all_car':all_car,
        # 'search_fields':search_fields,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style':body_style,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def cars(request):
    return render(request,'pages/cars.html')

def contact(request):
    return render(request,'pages/contact.html')

