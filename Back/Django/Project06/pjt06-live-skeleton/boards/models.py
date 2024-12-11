from django.db import models 
from django.conf import settings #유저


# Create your models here.
class Board(models.Model):
    #관계형 데이터 베이스 -> board == 있는 사람만 만들도록 한다.
    #보드 입장에서 작성자가 여러명일 수 있을까? = X
    #하나당 여러개일수 없다 -> user 입장에서는 가능 O 
    #1:N이라 foreginkey
    #아무것도 하지 않는게 있을 수 있음

    #유저가 지워졌을 때 어떻게 작업을 할까? == 없는 데이털르 참조하게 되는데 말이안되지 않는가?
    #유저 탈퇴시 DB에서 잘 안날린다. => 그럼 어떻게 작업을 하는가?? QQQ? 
    #활성화된 유저인가 확인하고 탈퇴하게 됨 == 탈퇴한 사람 == 비활성화 걸어버림

    #admin 변경?? QQ => 
    #set_null ??QQ  => 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='boards') #같이지우는 cascade
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments') #같이지우는 cascade
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)