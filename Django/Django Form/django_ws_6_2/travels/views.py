from django.shortcuts import render, redirect
#모델에서 원하는 값을 얻어와야함
from .models import Travels
#form에 대한 정보도 생성해야 함
from .forms import TravelsForm

# Create your views here.
def index(request):
    travels = Travels.objects.all() #모든 정보를 얻을 것이기 떄문
    context = { #dict형태로 인자를 전달함
        'travels' : travels
    }
    return render(request, 'travels/index.html', context) #인자 제공

def create(request):
    if request.method == "POST":
        form = TravelsForm(request.POST) #에 결과값을 받아서 그것을 저장할것이다.
        if form.is_valid():
            form.save() #맞다면 저장을하고
            return redirect('travels:index') #main 화면으로
    else : 
        form = TravelsForm()
    context = {
        'form' : form
    } #페이지 폼에 대한 주소를 보내준다.
    return render(request, 'travels/new.html', context) #폼에 대한 주소를 보내준다.

def detail(request, pk): #상세 내역을 뽑아옴 -> 이건 form양식 X
    travel = Travels.objects.get(pk=pk) #특정 데이터를 뽑아서 -> 그것을 활용할 것
    context = {
        'travel' : travel
    } #상세 페이지로 랜더링
    return render(request, 'travels/detail.html', context)


# def new(request): #form으로 보내줄 것이다.
#     #form에 대한 것을 받아서 -> context로 보여줄 것이다.
#     form = TravelsForm()
#     context = {
#         'form' : form
#     } #페이지 폼에 대한 주소를 보내준다.
#     return render(request, 'travels/new.html', context) #폼에 대한 주소를 보내준다.

# def create(request): #create한 것을 redirect로 메인 화면에 보여준다. -> 즉 메인 화면으로 보내는게 아니라
#     #받아서 다시 한 번 더 요청해준다 :: 그게 메인화면으로 간다.
#     #요청받은 POST결과가 form 태그에 정보를 받아서 들어올 것
#     form = TravelsForm(request.POST) #에 결과값을 받아서 그것을 저장할것이다.
#     #단 유효성 검사를 진행해야 함
#     if form.is_valid():
#         form.save() #맞다면 저장을하고
#         return redirect('travels:index') #main 화면으로
#     #그게 아니라면
#     context = {
#         'form' : form #내용을 받아서
#     } #다시 생성 페이지로 가서 수정을 해라
#     return render(request, 'travels/new.html', context) #context 파일을 보내면서요