from django.db import models

# Create your models here.
# model 설정 -> 일단은 관계형 데이터베이스 설계를 위한 데이터만 작성한다
class Author(models.Model): #저자 정보에서 각 저자의 이름이 표기 되도록 해야 한다.
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()
    nationality = models.TextField()
    #author를 부르면 -> 저자의 이름이 나올 수 있또록
    def __str__(self):
        return self.name #이름을 불러준다. ==> 저자 목록에서 각 저자의 이름이 표기되도록
    

#저자가 한명

#여러개의 책을 쓸 수 있으니까 
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #1대 N관계를 맺는다. 
    title = models.CharField(max_length=100)
    description = models.TextField()
    adult = models.BooleanField()
    price = models.IntegerField()