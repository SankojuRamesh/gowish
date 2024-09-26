# Generated by Django 5.0.7 on 2024-09-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatemanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatemodel',
            name='template_small_thumb',
            field=models.ImageField(default=None, upload_to='template_thumbs/'),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
