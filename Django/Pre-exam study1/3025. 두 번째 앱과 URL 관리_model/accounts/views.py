from django.shortcuts import render

# Create your views here.
def login(request): #단순 request
    return render(request, 'accounts/index.html')