# Generated by Django 3.2.8 on 2021-11-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_modelwithfilefield_article_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='modelwithfilefield',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
