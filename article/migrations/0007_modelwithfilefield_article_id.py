# Generated by Django 3.2.8 on 2021-11-02 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20211101_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelwithfilefield',
            name='article_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.article'),
        ),
    ]
