# Generated by Django 3.0.14 on 2021-10-22 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
        ('matces', '0003_auto_20211022_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='matces',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tournament.Tounament'),
        ),
    ]
