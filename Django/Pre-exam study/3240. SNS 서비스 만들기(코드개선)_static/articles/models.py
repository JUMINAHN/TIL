from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='%YY/%mm/%dd/') #중간 중간에 슬래쉬
    image_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)