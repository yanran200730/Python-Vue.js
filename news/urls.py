from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
    url(r'^api/article_list$', views.article_list),
]