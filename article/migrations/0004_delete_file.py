# Generated by Django 3.2.8 on 2021-11-01 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]
