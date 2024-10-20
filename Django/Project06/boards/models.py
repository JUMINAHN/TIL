from django.db import models
from django.conf import settings


# Create your models here.
class Board(models.Model):
    #게시글과 user 참조 진행 중
    #외래키로 1대 N 관계 진행 중인 것을 알 수 있음
    #board즉 게시판에서 사용자를 조회한다면 => board = Board.objects.get(pk=pk)
    #board.author를 통해 조회할 수 있음 ==> 단 사용자가 board를 참조하려면?
    #author.board_set.all()을 진행해야 한다는 의미
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='board') #이미 역참조화
    #명확한 구분을 위해 related_name 설정 
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    #자 댓글을 보면 => 댓글로 저자에 접근하려면
    #상기 게시글에서 진행한 것과 동일하게 진행하면 됨 comment = Comment.Object.get(pk=pk)
    #댓글을 쓴 저자 접근 == comment.author
    #단, 역참조 => 저자가 쓴 댓글 모두 참고 == author.comment_set.all() => realted 설정했으니 author.usercomment.all()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='usercomment') 
    #자 여기서도 게시글은 하나이지만 댓글이 여러개일 수 있음
    #comment.board로 접근하면 => 댓글이 달린 보드 == 해당 댓글이 있는 보드
    #board.comments.all() => 보드에 있는 댓글 전체 
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    #대댓글 관련된 내용인 것 같음
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)