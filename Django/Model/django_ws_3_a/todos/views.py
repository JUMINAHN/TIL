from django.shortcuts import render

# Create your views here.
# def index(request):
#     work = request.GET.get('work')
#     context = {
#         'work': work
#     }
#     return render(request, 'index.html', context)

# def create_todo(request):
#     return render(request, 'create_todo.html')

# def detail(request, work):
#     context = {
#         'work': work
#     }
#     return render(request, 'detail.html', context)

#views때문이 아닐까?
def index(request):
    work = request.GET.get('work')
    context = {
        'work': work
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, work):
    context = {
        'work': work
    }
    return render(request, 'todos/detail.html', context)