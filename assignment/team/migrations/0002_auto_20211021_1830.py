# Generated by Django 3.2.8 on 2021-10-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='role_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
