# Generated by Django 5.0.7 on 2024-09-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]