# Generated by Django 3.1 on 2020-08-29 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic.png', null=True, upload_to='profile_pics'),
        ),
    ]
