# Generated by Django 3.2.8 on 2021-10-28 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Users',
            new_name='user',
        ),
    ]
