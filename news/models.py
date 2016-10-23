from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    newsItem = models.CharField("新闻分类", max_length=50)
    article  = models.TextField("正文")
    title    = models.CharField("标题", max_length=50)
    created     = models.DateTimeField(default=timezone.now)
    author    = models.CharField("新闻出处", max_length=50)   
    imgs     = models.TextField("图片") 

    def __str__(self):
        return self.author + "  -------------  " + self.title

    class Meta:
        ordering = ["-created"]

class Links(models.Model):
    links = models.CharField("新闻链接", max_length=200)

    def __str__(self):
        return "新闻链接"
        