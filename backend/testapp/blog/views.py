from django.shortcuts import render
from .models import Article, Name
from .serializers import ArticleSerializer, NameSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

class NameView(RetrieveUpdateAPIView):

  queryset = Name.objects.all()
  serializer_class = NameSerializer

class ArticleListView(ListCreateAPIView):

  queryset = Article.objects.all().order_by('-id')
  serializer_class = ArticleSerializer

class ArticleSingleView(RetrieveUpdateDestroyAPIView):

  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  