from django.shortcuts import render

# Create your views here.
def introduce(request, username):
    context = {
        'username' : username,
    }
    return render(request, 'my_app/introduce.html', context) #url, 그리고 contents -> username을 받을 수 있어야 함