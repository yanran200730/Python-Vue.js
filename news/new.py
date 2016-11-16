import requests
import json
from bs4 import BeautifulSoup
import os
import sys
import re
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
                    print ("新闻链接 ----------" + link)
                else:
                    continue
            else:
                newsLinks.append(link)
                Links.objects.create(links=link) 
                flag = True  
                print ("新闻链接 ----------" + link)           
                # break
    print ("新闻链接总数------" + str(len(newsLinks)))
    print (len(soups))
    return newsLinks

def downloadImageFile(imgUrl):
    """下载图片并已图片名保存"""
    # local_filename = "/".join(imgUrl.split('/')[-2:]) 
    local_filename = imgUrl.split('/')[-1]  
    print ("图片下载中-----", local_filename,imgUrl) 
    r = requests.get(imgUrl, stream=True) 
    with open("../vue2.0/static/img/"+local_filename, 'wb') as f:  
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
    for newsLink in newsLinks:
        imgs = []
        print (newsLink)
        try:
            newsRequest = requests.get(newsLink)
            newsRequest.raise_for_status() 
        except requests.RequestException as e:
            print (e)
        else:
            newsSoup = BeautifulSoup(newsRequest.content, "html.parser")
            tag = newsSoup.select("#article ol a")[1].string
            title = newsSoup.select("#article .article_header > h1")[0].string
            user = newsSoup.select("#article .auther")[0].string
            imgLinks = newsSoup.select(".article_content > #content img")
            for imgLink in imgLinks:
                if imgLink.get("data-original"):
                    imgs.append(imgLink.get("data-original"))
                    downloadImageFile(imgLink.get("data-original"))                   
                else:
                    imgs.append(imgLink.get("src"))
                    downloadImageFile(imgLink.get("src"))
            content = ""
            imgStr = ""
            if len(imgs)<1:
                imgStr = "/static/img/me.jpg" 
            else: 
                imgStr = "/static/img/" + imgs[0].split("/")[-1]
            newsContent = str(newsSoup.select("#article #content")[0])
            if "http://zkres2.myzaker.com" in newsContent or "http://zkres1.myzaker.com" in newsContent:
                content1 = newsContent.replace("http://zkres2.myzaker.com","/static/img").replace("http://zkres1.myzaker.com","/static/img").replace("/img_upload/cms/article_img/ckeditor","").replace("/img_upload/cms/ck/img","")
                content2 = content1.replace("data-original","src").replace("/data/attachment/editor","")
                r = re.compile("2\d{5}/")
                r1 = re.compile("\d+/\d+/\d+/\d+/")
                r2 = re.compile("\d+/\d+/\d+/")
                content3 = r.sub("",content2)
                content4 = r1.sub("",content3)
                content = r2.sub("",content4)
            else:
                content = newsContent
            News.objects.create(newsItem=tag, article=content, title=title, author=user, imgs=imgStr)

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




