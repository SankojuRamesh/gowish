# Generated by Django 5.0.7 on 2024-09-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storemanager', '0002_storemodel_email_storemodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='storemodel',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
