from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)
    

def create(request): #얘로 기능이 옮겨진다.
    if request.method == 'POST': #영역을 나눌떄 -> request == post로 
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('reservations:index')
    else : #
        form = ReservationForm()
        context = {
            'form': form
        }
    return render(request, 'reservations/create.html', context)

        
    
