# Generated by Django 3.2.4 on 2024-07-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0005_users_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='education',
            field=models.CharField(default='', max_length=255),
        ),
    ]
