# Generated by Django 3.2.8 on 2021-11-16 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0017_alter_article_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章发布', 'verbose_name_plural': '文章发布'},
        ),
        migrations.AlterModelOptions(
            name='modelwithfilefield',
            options={'verbose_name': '文件管理', 'verbose_name_plural': '文件管理'},
        ),
        migrations.AlterModelOptions(
            name='usercomment',
            options={'verbose_name': '评论管理', 'verbose_name_plural': '评论管理'},
        ),
        migrations.AddField(
            model_name='usercomment',
            name='publish_date',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='正文内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=120, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='modelwithfilefield',
            name='file_field',
            field=models.FileField(null=True, upload_to='upload', verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='modelwithfilefield',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='comment',
            field=models.TextField(verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='user_id',
            field=models.CharField(max_length=100, null=True, verbose_name='用户名'),
        ),
    ]
