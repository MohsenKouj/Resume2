# Generated by Django 3.2.4 on 2024-07-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0002_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
