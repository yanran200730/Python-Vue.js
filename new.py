import requests
from bs4 import BeautifulSoup

# with open('test.txt','w',encoding='utf-8') as f:
#     f.write(page.text)
def getPage(navBar):
    pages = list()
    soups = list()
    for navItem in navBar:
        pages.append(navItem.get("href"))
        for page in pages:
            soups.append(BeautifulSoup(requests.get(page).content, "lxml"))
    print (len(soups))
    return soups      

def getNewsLinks(soups):
    newsLinks = list()
    for soup in soups:
        sections = soup.select("#content #section a")
        for links in sections:
            link = links.get("href")
            if link not in newsLinks:
                newsLinks.append(link)
                print ("新闻链接 ----------" + link)
    print ("新闻链接总数------" + str(len(newsLinks)))
    return newsLinks
    
def main(url):
    homePage = requests.get(url).content
    homeSoup = BeautifulSoup(homePage, "lxml")
    navBar = homeSoup.select(".nav a")
    soups = getPage(navBar)
    return getNewsLinks(soups)

links = main("http://www.myzaker.com/")



