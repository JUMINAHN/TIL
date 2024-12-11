from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_http_methods(["GET"]) #api_view => decorations을 사용했었음
# boards = get_list_or_404() : 데이터가 없을 때 404 error을 띄워준다 == 있는지 없는지 분리해주는게 좋음
# - 데이터가 없어도 화면측에서 사용자에게 알림을 줄 수 있다면 사용 가능
# - 프론트 측(django에선 tempalte)에서 404 error를 처리해줬다면 사용 가능
# django ORM -> SQL 변환
def index(request): #에러를 안띄웠다면 오더바이
    boards = Board.objects.all().order_by('-created_at') #?showmigrations, sqlmigrate => 어떤 sql로 사용되었는지
    #추적할 수 있다
    context = {
        'boards': boards
    }
    return render(request, 'boards/index.html', context)

@require_http_methods(["GET", "POST"])
def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')

    comments = board.comments.all()
    comment_form = CommentForm()
    
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)


@require_http_methods(["GET", "POST"])
@login_required
def update(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'board': board,
        'form': form,
    }        
    return render(request, 'boards/update.html', context)


@require_http_methods(["GET", "POST"])
@login_required
def create(request): #index, create 따로 합치기 힘들어서 
    # if.request.user.is_authenticated : 튕기도록
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context) #rendering해줘야 함
    #rest_api는 따로 쓸필요가 없음
    #우리는 rendering을 해야하기 때문에 create와 index를 만든다.

@require_http_methods(["POST"])
@login_required
def comment(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
            return redirect('boards:detail', board.pk)

@require_http_methods(["POST"])
@login_required
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)