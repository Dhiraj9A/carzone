from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.order_by('-created_date')
    data={
        'teams':teams,
        'featured_car':featured_car,
        'all_car':all_car,
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
