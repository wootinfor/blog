from os import truncate
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User

import article,os


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Article(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='序号')
    title = models.CharField(max_length=120,verbose_name='标题')
    content = models.TextField(verbose_name='正文内容')
    publish_date = models.DateTimeField(auto_now=True,verbose_name='发布时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,verbose_name='用户名')
    # user = models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name='文章发布'
        verbose_name_plural='文章发布'


    def __repr__(self):
        return Article.title

    def short_content(self):
        return self.content[:50]
    def __str__(self):
        return self.title

    short_content.short_description = 'content'


# Create your models here.
class ModelWithFileField(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='序号')
    file_field=models.FileField(upload_to='upload',null=True,verbose_name='文件')
    article_id=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    user_id=models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name='文件管理'
        verbose_name_plural='文件管理'

    def __str__(self):
        return self.file_field.name[-20:]

class userComment(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='序号')
    comment=models.TextField(verbose_name='评论')
    article_id=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    user_id=models.CharField(max_length=100,null=True,verbose_name='用户名')

    class Meta:
        verbose_name='评论管理'
        verbose_name_plural='评论管理'

    def __str__(self):
        return self.comment[:20]