from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    #img 필드 사용을 위해선 pillow 라이브러리가 필요하다.
    image = models.ImageField(blank=True, upload_to='images/') #imagefield blank여도 된다 -> 항상 참이 아니기 때문에
    #models image를 설정하고 -> pillow 설치 -> 이미지에 대한 migration 진행
    #어디로 업로드할것인지 -> 거기에 대한 경로까지 form에 남겨줌으로써 데이터 활용할 수 있도록

    #미디어 파일 추가 경로 작성