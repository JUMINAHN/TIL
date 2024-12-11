from django.shortcuts import render

# Create your views here.

def introduce(request, name): #매개변수와 함께 username을 받을 수 있어야 함
    #templates는 표기할 필요가 없기때문에 상기처럼 작성한다.
    context = {
        'name' : name,
    }
    return render(request, 'my_app/introduce.html', context) #site url을 작성해야 함
    #site url은 templates/my_app/introduce.html이어야 한다.
    #즉 templates를 생성하고, 하위 폴더 my_app 아래에 introduce html을 생성해야 함
