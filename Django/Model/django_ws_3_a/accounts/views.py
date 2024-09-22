from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html') #앱의 탬플릿 규칙을 생각하기