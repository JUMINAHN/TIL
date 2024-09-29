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

def detail(request, pk): #상세페이지 => 그냥 단순 pk로 정보 받아와서 진행 :: 기존과 동일하게 하면 됨 -> form과 무관
    garage = Garage.objects.get(pk=pk) #pk 정보를 받아서 -> 해당 정보 확인하기
    #context로 내보내기 -> 활용을 위해서
    context = {
        'garage' : garage
    }
    return render(request, 'garages/detail.html', context)

def delete(request, pk): #특정정보를 받아서 삭제해야하기 떄문에 -> 해당 정보를 받아서 삭제하고 redirect로 다시 메인 페이지를 요청해주면 됨
    garage = Garage.objects.get(pk=pk)
    garage.delete()
    return redirect('garages:index') #mainpage로 다시 돌려주기

#업데이트 하기
def edit(request, pk) : #특정항목 업데이트하기 -> create와 동일한 구조를 띄고 있음
    #pk의 정보를 받아서 새로운 데이터들을 넣을 것 -> 일단 이건 form에 대한 링크만 보내줄 것임
    #특정 페이지와 관련된 내용이 들어가긴 해야하니까 데이터를 담아서 다시 넣어서 전달해줌
    garage = Garage.objects.get(pk=pk)
    context = {
        'garage' : garage
    }
    return render(request, 'garages/edit.html', context) #form의 정보를 주지만 기존의 데이터를 기반으로 특정 데이터임을 명시해줘야 함

#업데이트하기 -> post로 요청받은 것 다시 반영해서 사용해야 함 == 기존 create와 동일하게 작업될 것
def update(request, pk): 
    garage = Garage.objects.get(pk=pk) #특정 정보
    garage.location = request.POST.get('location')
    garage.capacity = request.POST.get('capacity')
    garage.is_parking_avaliable = request.POST.get('is_parking_avaliable')
    garage.opening_time = request.POST.get('opening_time')
    garage.closing_time = request.POST.get('closing_time')

    #새로운 정보 갱신한 것
#    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save() #다시 저장하고 -> 원본 페이지로 다시 돌려준다. #-> 상세 페이지로 돌려주려면 다시 pk 정보나 context로 내용을 돌려줘야함
    #ex) garage.pk
    return redirect('garages:index')