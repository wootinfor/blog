from os import truncate
from django.db import models
from django.db.models.fields import IntegerField

import article,os


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish_date = models.DateTimeField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __repr__(self):
        return Article.title

    def short_content(self):
        return self.content[:50]
    def __str__(self):
        return self.title

    short_content.short_description = 'content'

# Create your models here.
class ModelWithFileField(models.Model):
    id=models.AutoField(primary_key=True)
    file_field=models.FileField(upload_to='upload',null=True)
    article_id=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    user_id=models.CharField(max_length=100,null=True)

class userComment(models.Model):
    id=models.AutoField(primary_key=True)
    comment=models.TextField()
    article_id=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    user_id=models.CharField(max_length=100,null=True)