from django.shortcuts import render

# Create your views here.
#index view 함수 수정 -> 전달받는 구역
def index(request): #variable routing으로 form이 아닌 것에서 전달해줄 떄 매개변수로 work를 받음
    work = request.GET.get('work') #form으로 전달받을때는 variable routing과 다르게 동작한다.
    context = {
        'work' : work,
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')