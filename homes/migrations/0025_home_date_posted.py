# Generated by Django 3.1 on 2020-09-11 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0024_auto_20200911_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]