# Generated by Django 5.0.7 on 2024-09-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorymanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategorymodel',
            name='image_thumbnail',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='subcategorymodel',
            name='video_thumbnail',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
