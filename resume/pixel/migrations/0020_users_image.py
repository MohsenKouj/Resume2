# Generated by Django 3.2.4 on 2024-07-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0019_auto_20240711_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(default='posts-img/upic.png', max_length=255, upload_to='posts-img'),
        ),
    ]
