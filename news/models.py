from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    newsItem = models.CharField("新闻分类", max_length=50)
    article  = models.CharField("正文")
    title    = models.CharField("标题", max_length=50)
    time     = models.DateTimeField(default=timezone.now)
    users    = models.CharField("新闻出处", max_length=50)   
    imgs     = models.CharField("图片") 