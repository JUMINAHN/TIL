from django.db import models
#일단 해당 문제 요구 조건은 static을 사용하지 않아도됨

# Create your models here.
class Article(models.Model): #model -> class 생성
    title = models.CharField(max_length=100)
    #image 필드가 아니라 filefield
    #사용자가 업로드한 이미지를 저장할 수 있어야 한다.
    #업로드 자체의 경로는 media로 한다. 
    content = models.CharField(max_length=250)
    image = models.FileField(blank=True, upload_to='images/') #blank 해도 됨
    #난 약간 추가적으로 구체적인 경로를 'images/'로 설정하고자 함
    image_description = models.TextField()
    is_public = models.BooleanField(default=True) #default true를 하면 check가 되지 않을까?
    created_at = models.DateTimeField(auto_now_add=True)
