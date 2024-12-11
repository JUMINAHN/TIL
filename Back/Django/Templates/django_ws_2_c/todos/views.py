from django.shortcuts import render

# Create your views here.
def index(request):
    work = request.GET.get('work')
    context = {
        'work': work
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

#work 경로 요청을 보낼 경우 detail함수가 실행
def detail(request, work): #일단 todos/work니까 그대로 쓴다, variable routing은 두번째 인자를 넣어야 한다.
    #work = request.GET.get('work')
    context = {
        'work' : work, #바로 그냥 work 사용, work 인자를 받아서
    }
    return render(request, 'todos/detail.html', context) #만들 것임, detail.html -> detail함수 실행 및 경로를 보고 설정