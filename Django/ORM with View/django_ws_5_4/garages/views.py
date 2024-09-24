from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request): #여기서 all로 모든 정보를 받아와야한다.
    garages = Garage.objects.all() #모든 정보 받아`오기
    context = {
        'garages' : garages
    }
    return render(request, 'garages/index.html', context) #모든 정보를 확인할 수 있어야 한다.

def new(request):
    return render(request, 'garages/new.html') #form 작성 링크 전달

def create(request):
    location = request.POST.get('location') #post방식으로 받았다.
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save() #save()로 데이터에 저장했다.
    return redirect('garages:index') #메인 페이지로 redirect하기 위함
    #redirect는 index 첫번째 페이지로