from django.db import models

# Create your models here.
#content / picture인데 왜 work, content만 뜨는거지? == diary
class Diary(models.Model):
    content = models.CharField(max_length=125)
    #날짜 표기 양식?
    picture = models.ImageField(blank=True, upload_to='%Y/%b/%a/') #년/월/요일로갈 수 있도록 -> 이거 이름 확인
    created_at = models.DateTimeField(auto_now_add=True)