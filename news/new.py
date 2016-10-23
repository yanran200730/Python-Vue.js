import requests
import json
from bs4 import BeautifulSoup
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
sys.path.append(os.path.dirname(__file__))

from news.models import News
from news.models import Links

# with open('test.txt','w',encoding='utf-8') as f:
#     f.write(page.text)
def getLinksField():
    LinkList = list()
    LinkFields = Links.objects.all()
    if len(LinkFields) < 1:
        return False
    for i in LinkFields:
        LinkList.append(i.links)
    return LinkList


def getPage(navBar):
    """获取指令分类的新闻页面"""
    items = ["热点","娱乐","体育","科技","互联网","科学","美食","电影","社会","星座"]
    soups = list()
    for navItem in navBar:
        if navItem.string in items:
            page = navItem.get("href")
            print (page, navItem.string)
            try:
                itemRequest = requests.get(page, timeout=10)
                itemRequest.raise_for_status()
            except requests.RequestException as e:
                print (e)
            else:
                soups.append(BeautifulSoup(itemRequest.content, "html.parser"))
                # break
    return soups      

def getNewsLinks(soups):
    """获取新闻页面的新闻链接"""
    newsLinks = list()
    flag = False
    for soup in soups:
        sections = soup.select("#content #section a")
        for links in sections:
            link = links.get("href")
            if (flag):
                LinkList = getLinksField()
                if link not in newsLinks and link not in LinkList:
                    newsLinks.append(link)
                    Links.objects.create(links=link)
                    print ("新闻链接 ----------222" + link)
                else:
                    continue
            else:
                newsLinks.append(link)
                Links.objects.create(links=link) 
                flag = True  
                print ("新闻链接 ----------111" + link)           
                # break
    print ("新闻链接总数------" + str(len(newsLinks)))
    print (len(soups))
    return newsLinks

def downloadImageFile(imgUrl):
    """下载图片并已图片名保存"""
    local_filename = imgUrl.split('/')[-1]  
    print ("图片下载中-----", local_filename,imgUrl) 
    r = requests.get(imgUrl, stream=True) 
    with open("../vue2.0/src/assets/"+local_filename, 'wb') as f:  
        for chunk in r.iter_content(chunk_size=1024):  
            if chunk:  
                f.write(chunk)  
                f.flush()  
        f.close()  
    return local_filename  

def getNewsInfor(newsLinks):
    """获取新闻信息,并存入数据库"""
    news = []
    newDict = {}
    imgs = []
    for newsLink in newsLinks:
        print (newsLink)
        try:
            newsRequest = requests.get(newsLink)
            newsRequest.raise_for_status() 
        except requests.RequestException as e:
            print (e)
        else:
            newsSoup = BeautifulSoup(newsRequest.content, "html.parser")
            newDict["tag"] = newsSoup.select("#article ol a")[1].string
            newDict["title"] = newsSoup.select("#article .article_header > h1")[0].string
            newDict["user"] = newsSoup.select("#article .auther")[0].string
            imgLinks = newsSoup.select(".article_content > #content img")
            for imgLink in imgLinks:
                if imgLink.get("data-original"):
                    imgs.append(imgLink.get("data-original"))
                    downloadImageFile(imgLink.get("data-original"))                   
                else:
                    imgs.append(imgLink.get("src"))
                    downloadImageFile(imgLink.get("src"))                    
            newDict["imgs"] = imgs
            newsContent = str(newsSoup.select("#article #content")[0])
            if "http://zkres2.myzaker.com" in newsContent or "http://zkres1.myzaker.com" in newsContent:
                content1 = newsContent.replace("http://zkres2.myzaker.com","http://127.0.0.1:8000/static")
                content2 = content1.replace("http://zkres1.myzaker.com","http://127.0.0.1:8000/static")
                content  = content2.replace("data-original","src")
            newDict["content"] = content
            News.objects.create(newsItem=newDict["tag"], article=newDict["content"], title=newDict["title"], author=newDict["user"], imgs=newDict["imgs"])

def main(url):
    try:
        homRrequest = requests.get(url, params={'ip': '8.8.8.8'}, timeout=10)
        homePage = homRrequest.content
        homRrequest.raise_for_status()
    except requests.RequestException as e:
        print (e)
    else:
        homeSoup = BeautifulSoup(homePage, "html.parser")
        navBar = homeSoup.select(".nav_item,.nav_menu_item")
        soups = getPage(navBar)
        newsLinks = getNewsLinks(soups)
        getNewsInfor(newsLinks)

links = main("http://www.myzaker.com/")




