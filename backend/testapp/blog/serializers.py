from rest_framework import serializers
from .models import Name, Article 

class NameSerializer(serializers.ModelSerializer):

  class Meta:
    model = Name
    fields = ('pk', 'value')

class ArticleSerializer(serializers.ModelSerializer):

  class Meta:
    model = Article
    fields = ('pk', 'title', 'body', 'date')