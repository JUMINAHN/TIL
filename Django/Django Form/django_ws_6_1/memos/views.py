from django.shortcuts import render,redirect
from .models import Memos #memo라는 모델을 가져온다.
from .forms import MemosForm

# Create your views here.
# view에서 함수를 생성한다.
# migrations을 요구조건대로 하려고 했지만 -> veiw함수가 없어서 생성되지 않음
def index(request): #index에서 값을 보여줄 것
    #구조적으로 보았을 떄 전체 database에 있는 내용을 가져와야함을 알 수 있음 -> 따라서 model을 호출한다.
    memos = Memos.objects.all() #memo object를 가져올 것이고, 이거를 dict로 보내야 index에서 사용 가능
    context = {
        'memos' : memos
    }
    return render(request, 'memos/index.html', context) #views는 특정 html로 보내게 한다. -> 랜더링을 위해서
    #구조를 생각해보면 views가 html과 상호작용하기 떄문에 -> 이렇게 전달하면

#이제 통합
def create(request) : 
    if request.method == "POST": #method가 post일 떄
        form = MemosForm(request.POST) 
        if form.is_valid(): #이게 유효하다면
            form.save() #저장하고 -> 맞게 redirect로 돌려준다.
            return redirect('memos:index')
    else :
        form = MemosForm() 
    context = {
        'form' : form    
    }
    return render(request, 'memos/create.html', context) #form을 사용하기 위해서

# 상세정보 생성 => detail form에서 정보를 받아올 것
def detail(request, pk): #기존과 동일하게 작업을 진행했던 것 같음 -> 생성/수정의 부분만 금일 건들였기 떄문에
    #기존과 동일하게 get으로 pk를 받아온다.
    memo = Memos.objects.get(pk=pk) #pk를 받아오고 -> 해당 부분을 활용할 것
    context = {
        'memo' : memo
    } #detail 상세 페이지로 돌려주고, 랜더링 해줄것, 단순히 상세 페이지를 보여주는 역할만 있기 때문에
    return render(request, 'memos/detail.html', context)

def delete(request, pk): #이것은 redirect로 메인 화면으로 보여줄 것
    #form으로 요청 특정 객체를 받아와서 삭제를 한다. -> detail과 동일해
    memo = Memos.objects.get(pk=pk)
    memo.delete() #삭제하고
    return redirect("memos:index") #main 화면으로 보내준다.

# def create(request) : #이건 받아서 -> 메인페이지 맞게 띄웠는지 확인하는 것 : 생성하고 메인 페이지로
#     #단 이것은 유효성 검사가 타당했을때임
#     #하지만, 유효성 검사가 타당하지 않았을떄는 다시 new page로 들어가서 생성의사를 다시 물어봐야함
#     #post의 유무로 확인을 하는데 아직 합치기 전이라서 일단 이렇게하고
#     #memosform으로 요청받은 내용을 받아서 저장하고 유효성 검사를 해야한다.
#     ## 기존과 똑같이 불러오되, 거기에 request.POST만 확인하면 된다.

#     form = MemosForm(request.POST) 
#     if form.is_valid(): #이게 유효하다면
#         form.save() #저장하고 -> 맞게 redirect로 돌려준다.
#         return redirect('memos:index') #index 페이지로 돌려줄거에요
#     #그게 아니라면 context를 전달해서 다시 글을 쓰도록 new page로 돌려준다.
#     context = {
#         'form' : form
#     }
#     return render(request, 'memos/new.html', context) #어디로 보내냐?