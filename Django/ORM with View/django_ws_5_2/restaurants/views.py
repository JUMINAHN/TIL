from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request): 
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(reqeust):
    restaurant = Restaurant()
    restaurant.name = reqeust.POST.get('name')
    restaurant.description = reqeust.POST.get('description')
    restaurant.address = reqeust.POST.get('address')
    restaurant.phone_number = reqeust.POST.get('phone_number')
    restaurant.save()
    return redirect('restaurants:index')

#상세정보 관련해서 내용을 보여준다.
#그 정보를 받아서 display해야한다.
#variable routing
def detail(request, pk): #pk 정보를 기반으로
    restaurants = Restaurant.objects.get(pk=pk) #pk 정보를 받아서
    context = {
        'restaurants' : restaurants
    }
    #상세 정보 페이지를 보여줄 것이기 때문에
    return render(request, 'restaurants/detail.html', context)

#delete로 데이터 삭제
#create와 비슷하게 접근하면 된다. 특정 데이터 받아와서 삭제
def delete(request, pk): #create처럼
    restaurants = Restaurant.objects.get(pk=pk) #pk 정보 받아와서 삭제
    restaurants.delete() #삭제하고 -> redirect -> 어떤 페이지로 ?
    return redirect('restaurants:index') #main page로 다시 돌려준다

def edit(request, pk): #edit는 context를 가져와야 할 것 같음
    #즉 기존에 new에서 사용했던 form양식을 그대로 사용하면 될 것 같음
    restaurants = Restaurant.objects.get(pk=pk)
    context = { #왜냐하면 기존 pk내용을 받아서 화면에 띄워야하기 떄문에
        'restaurants' : restaurants 
    }
    return render(request, 'restaurants/edit.html', context) #그 사이트에서 수정을 해야하기 떄문에

#update도 create의 post방식을 가져오면 될 것 같음
def update(reqeust, pk): #인자가 없다? -> url도 보면 매개변수 인자를 필요로 하는 것을 볼 수 있음
    restaurant = Restaurant.objects.get(pk=pk) #object를 필요로함
    restaurant.name = reqeust.POST.get('name')
    restaurant.description = reqeust.POST.get('description')
    restaurant.address = reqeust.POST.get('address')
    restaurant.phone_number = reqeust.POST.get('phone_number')
    restaurant.save() #다시 받아서 저장하고
    return redirect('restaurants:index') #요구 조건에 따르면 메인 페이지로 보내길 원함
