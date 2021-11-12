# Generated by Django 3.2.8 on 2021-11-01 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_modelformwithfilefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithFileField',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('file_field', models.FileField(upload_to='upload')),
            ],
        ),
        migrations.DeleteModel(
            name='ModelFormWithFileField',
        ),
    ]