# Generated by Django 3.1 on 2020-09-05 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0017_auto_20200905_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='save',
            new_name='saves',
        ),
    ]
