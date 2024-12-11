from django.db import models

#이미지가 있는 경우에만 출력하도록 추후 html파일에서 설정 필요가 있음

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250) #widget로 추가 설정 필요
    image = models.FileField(blank=True) #추가 경로 설정없음-> 생략되어도 괜찮은 모델
    image_description = models.TextField()
    is_public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True) 