from django.shortcuts import render

# Create your views here.
# Attribute Error가 발생하는데 -> get을 찾아올 수 없다는 것
def index(request): #해당 함수를 수정하여 전송받은 데이터를 work변수에 할당한다.
    work = request.GET.get('work') #work로 받은 것, 전송 받은 데이터 --> Get이 아닌, GET :: 해당 값 주의
    context = {
        'work' : work, #17p -> 반대로 쓰고 있었다...! 오탈자 유의 ㅠㅠ
    }
    return render(request, 'todos/index.html', context) #create_todo로부터 전송받은 데이터를 work변수에 할당한다.

def create_todo(request):
    return render(request, 'todos/create_todo.html')