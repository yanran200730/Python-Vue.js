from .models import News
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	# author = serializers.ReadOnlyField(source='author.username')
	
	class Meta:    
		model = News
		fields = ('id','newsItem','article','title','created','author')

class ArticleListSerializer(serializers.HyperlinkedModelSerializer):
	# author = serializers.ReadOnlyField(source='author.username')
	
	class Meta:    
		model = News
		fields = ('id','newsItem','title','created','author','imgs')