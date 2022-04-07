from django.urls import path
from .views import * 

urlpatterns = [
  path(r'name/<int:pk>', NameView.as_view()),
  path(r'articles', ArticleListView.as_view()),
  path(r'articles/<int:pk>', ArticleSingleView.as_view())
]