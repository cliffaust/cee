# Generated by Django 3.1 on 2020-09-05 13:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homes', '0016_auto_20200905_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='save',
            field=models.ManyToManyField(related_name='saves', to=settings.AUTH_USER_MODEL),
        ),
    ]
