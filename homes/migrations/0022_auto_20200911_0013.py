# Generated by Django 3.1 on 2020-09-11 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0021_auto_20200907_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='lot_size',
            new_name='home_size',
        ),
    ]