from django.db import models

# Create your models here.
class APIinfo(models.Model):
    #url -> 경로를 저장한다는 것은 url을 사용한다는 의미
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(max_length=200)
    documentation_url = models.URLField(max_length=200)
    auth_required = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    additional_info = models.JSONField()