from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request):
    garages = Garage.objects.all()
    context = {
        'garages': garages
    }
    return render(request, 'garages/index.html', context)

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save()
    return redirect('garages:index')

#edit 편집할 정보 
#기존의 정보를 활용할 것
#그럼 특정 값에서 받아와야함
def edit(request, pk):
    garage = Garage.objects.get(pk=pk)
    context = {
        'garage' : garage #garage 특정 정보를 받아서 사용할 것이니까
    } #주소로 보내줄 것임
    return render(request, 'garages/edit.html', context) #new를 기반으로 동일하게 구조화하면 됨

#edit의 값을 form post로 받을 것 -> create와 동일하게 만들면됨
def update(request, pk): #일단 update인자가 2개이기 떄문에 받는다
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')
    #pk를 직접불러서 거기에 대한 값을 넣어야 할 것 같음
    garage = Garage.objects.get(pk=pk)
    garage.location = location
    garage.capacity = capacity
    garage.is_parking_avaliable = is_parking_avaliable
    garage.opening_time = opening_time
    garage.closing_time = closing_time

    # garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save() #수정 방식 변경
    return redirect('garages:index') #update idx로 하기 떄문에 돌려줄 필요가 없음

#delete 특정 값 받아서 
def delete(request, pk):
    garage = Garage.objects.get(pk=pk)
    garage.delete() #삭제를 한다.
    #redirect를 한다
    return redirect('garages:index') #여기 return값이 누락되었다..