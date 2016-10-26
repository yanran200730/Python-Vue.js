from django.shortcuts import render,HttpResponse
from .models import News
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import ArticleSerializer,ArticleListSerializer

def home(request):
    return render(request,"index.html")

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def article_list(request):
    # article = Article.objects.all()[0:1]
    news = News.objects.all()[0:10]
    serializer = ArticleListSerializer(news, many=True)
    response = JSONResponse(serializer.data)
    response['Access-Control-Allow-Origin'] = '*' #跨域
    return response

# def article_list(request):
#     sessionKey = 'article' + id
#     if request.session.get(sessionKey, False):
#         clickNumber = 0
#     else:
#         request.session[sessionKey] = 1
#         clickNumber = 1
#     article = Article.objects.get(id=str(id))
#     article.times = article.times + clickNumber
#     article.save()
#     serializer = ArticleSerializer(article)
#     response = JSONResponse(serializer.data)
#     response['Access-Control-Allow-Origin'] = '*' #跨域
#     return response