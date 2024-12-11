from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "chat/index.html")

#방번호를 매개변수로 받아줌
#key값으로 돌려줌 -> context 와 동일한 역할
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})