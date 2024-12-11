from django.shortcuts import render, redirect
from .models import Reservation
#form도 사용해야하니까 호출해야 함
from .forms import ReservationForm #이것도 해야함

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

#new에 대한 값을 써야 함
#new는 form에 대한 url만 보내는 곳
#form -> form url에서 확인하는 것
def new(request): #new에서도 사용할 것이기 때문에
    form = ReservationForm()
    context = { #context로 form에 대한 정보를 보내야 form을 사용할 수 있다.
        'form' : form,
    }
    return render(request, 'reservations/new.html', context)  #form 

def create(request): #create에 대한 내용
    #기존에는 request로 값을 하나씩 불러서 title을 넣고 save했던 형식
    #기존과 동일하게 진행하되, 이번에는 form 자체에서 제공하는 값을 전달받는다.
    form = ReservationForm(request.POST) #form.request -> form : 그냥 자체적으로 request Form
    #폼에서 요청값을 받아서
    if form.is_valid() :#유효성 검사
        reservation = form.save() #유효성이 맞으면 저장을 하고 
        return redirect('reservations:index') #main화면으로 돌려준다. #이때는 굳이 context를 사용하지 않기 때문에
       #create 만들고 -> mainpage로 돌려준다.
    context = {
        'form' : form,
    }
    return render(request, 'rservation/new.html', context)
    #안맞다면 -> 다시 돌아갑니다 -> 생성 페이지로
 