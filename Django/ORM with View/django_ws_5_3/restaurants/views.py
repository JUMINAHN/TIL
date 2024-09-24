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

def create(request):
    restaurant = Restaurant()
    restaurant.name = request.POST.get('name')
    restaurant.description = request.POST.get('description')
    restaurant.address = request.POST.get('address')
    restaurant.phone_number = request.POST.get('phone_number')
    restaurant.save() #그럼 자체적으로 pk 생성 -> 호출
    return redirect('restaurants:detail', restaurant.pk) #여기를 상세 페이지로 이동할 수 있도록 수정 -> 생성을 하고 바로 그 페이지로
    #왜 에러?

def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    context = {
        'restaurant' : restaurant
    }
    return render(request, 'restaurants/detail.html', context) 

def edit(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    context = {
        'restaurant' : restaurant
    }
    return render(request, 'restaurants/edit.html', context)

def update(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant.name = request.POST.get('name')
    restaurant.description = request.POST.get('description')
    restaurant.address = request.POST.get('address')
    restaurant.phone_number = request.POST.get('phone_number')
    restaurant.save()
    return redirect('restaurants:detail', restaurant_pk) #여기가 바껴야 함
    #reverse for 'detail' with no arguments not found. 
    #왜 에러?

def delete(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant.delete()
    return redirect('restaurants:index') #여기를 상세 페이지로 이동할 수 있도록 수정
    #이거는 detail일수가없음 -> 해당 페이지가 없거든..