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

def getNewsItem(string):
    items = {"redian":"热点","yule":"娱乐","tiyu":"体育","keji":"科技","hulianwang":"互联网","kexue":"科学","meishi":"美食","dianying":"电影","shehui":"社会","xingzuo":"星座"}
    return items[string]

def article_list(request):
    news = News.objects.all()
    index = int()
    NewsLists = list()
    if request.GET['item']:
        newsItem = request.GET['item']
    else:
        newsItem = "redian"
    item = getNewsItem(newsItem)
    if request.GET['page'] == 0:
        index = 0
    else:
        index = 10 * int(request.GET['page'])
    i = 0

    for new in news:
        if new.newsItem == item:
            NewsLists.append(new)
        else:
            continue
    serializer = ArticleListSerializer(NewsLists[index:index+10], many=True)
    response = JSONResponse(serializer.data)
    response['Access-Control-Allow-Origin'] = '*' #跨域
    return response

def article(request, id):
    article = News.objects.get(id=str(id))
    serializer = ArticleSerializer(article)
    response = JSONResponse(serializer.data)
    response['Access-Control-Allow-Origin'] = '*' #跨域
    return response
