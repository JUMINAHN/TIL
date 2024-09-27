from django.db import models

# Create your models here.
class Movie(models.Model): #model class 생성
    #영화 제목 줄거리 이미지
    #blank = True를 안했었는데 여기서 해야하니까 해서 넘어감..?
    title = models.CharField(max_length=20)
    content = models.TextField()
    img = models.FileField(blank=True, upload_to='images/')
    # img = models.ImageField(blank=True, upload_to='images/') #하면 됨