# Generated by Django 3.1 on 2020-09-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0020_auto_20200906_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecoordinate',
            name='latitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='homecoordinate',
            name='longitude',
            field=models.FloatField(blank=True),
        ),
    ]
