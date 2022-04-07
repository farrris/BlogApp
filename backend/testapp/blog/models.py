from django.db import models

# Create your models here.

class Article(models.Model):
  title = models.CharField('Title', max_length=500)
  body = models.CharField('Body', max_length=5000)
  date = models.CharField('Date', max_length=20)

  def __str__(self):
    return self.title
  
class Name(models.Model):
  value = models.CharField("Name", max_length=100, default='Это мой блог')

  def __str__(self):
    return self.value