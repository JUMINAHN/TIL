from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Board, Comment
from .forms import BoardForm, CommentForm


@require_http_methods(["GET"])
def index(request):
    boards = Board.objects.all().order_by('-created_at')
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


@login_required
@require_http_methods(["GET", "POST"])
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


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)


@login_required
@require_http_methods(["POST"])
def comment(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.author = request.user
            comment.save()
            return redirect('boards:detail', board.pk)
        

@login_required
@require_http_methods(["POST"])
def create_reply(request, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        reply_comment = form.save(commit=False)
        reply_comment.board = comment.board
        reply_comment.author = request.user
        reply_comment.parent_comment = comment
        reply_comment.save()
        return redirect("boards:detail", comment.board.id)


@require_http_methods(["POST"])
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)
    
#좋아요.. => 누르고, 취소할 수 있음 ==> 이것도 post가 딱히 필요없는 부분
#게시판 정보 받아오기
@login_required
def likes(request, board_pk):
    board = Board.objects.get(pk=board_pk) #특정보드
    #근데 board에 좋아요 눌러야하니까 => 일단 요청 유저와 board에 작성자가 달라야 함
    #board에서 작성자 확인
    if request.user != board.author: #이게 아니어야 좋아요 가능
        #board자체의 like_users에 접근 => 보드에 like_users를 한사람은 많을 것 :: 정참조
        #보드에 좋아요를 누른 유저 중 한명인가요?
        if request.user in board.like_users.all(): #그 중에서도 전체임을 호출해야 함
            #좋아요를 눌렀다면 취소
            board.like_users.remove(request.user) #여기서도 추가가능
        else :
            board.like_users.add(request.user)
    return redirect('boards:detail', board_pk)
