# Generated by Django 5.0.7 on 2024-08-29 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanager', '0002_alter_usermanager_options_usermanager_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermanager',
            name='name',
        ),
    ]