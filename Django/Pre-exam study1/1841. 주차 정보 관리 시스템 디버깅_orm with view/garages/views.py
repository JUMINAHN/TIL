from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request):
    garages = Garage.objects.all()
    context = {
        'garages' : garages
    }
    return render(request, 'garages/index.html', context) #있음  -> 전체 정보를 불러와야 함


def new(request): #form 정보 -> 
    return render(request, 'garages/new.html') #접속할 수 있는 주소

def create(request):
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save()
    return redirect('garages:index') #mainpage redirect