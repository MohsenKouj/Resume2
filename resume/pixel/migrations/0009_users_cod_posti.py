# Generated by Django 3.2.4 on 2024-07-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0008_users_t_p'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='cod_posti',
            field=models.CharField(default='', max_length=255),
        ),
    ]
