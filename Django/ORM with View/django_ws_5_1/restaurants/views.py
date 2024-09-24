from django.shortcuts import render, redirect
from .models import Restaurants

# Create your views here.
def index(request): #request, 전체 정보 받아와야 함
    restaurants = Restaurants.objects.all() #오타
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'restaurants/index.html', context)

def new(request) : #new는 그냥 form을 제공할 요소, 주소만 돌려줄 것
    return render(request, 'restaurants/new.html')

#create 그대로 post받은 내용을 저장한다.
def create(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    restaurant = Restaurants(name=name, address=address) #인자값안맞추면 오류
    restaurant.save() #저장하고  -> 저장한 값 출력을 위해 돌려준다
    #저장한 페이지 메인 화면으로 redirect
    return redirect('restaurants:index')