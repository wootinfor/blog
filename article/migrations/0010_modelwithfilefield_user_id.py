# Generated by Django 3.2.8 on 2021-11-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_modelwithfilefield_file_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelwithfilefield',
            name='user_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
