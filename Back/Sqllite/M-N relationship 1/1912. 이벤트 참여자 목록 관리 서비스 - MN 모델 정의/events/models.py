from django.db import models

# Create your models here.
#event와 participant -> M:N 관계 => 중개테이블은 직접 정의하지 않는다.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)

class Event(models.Model): #이벤트in에 참여한 참가자
    participant = models.ManyToManyField(Participant, related_name="in_participant")
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.TextField()

    #event로 participant 조회?