# Generated by Django 3.1 on 2020-09-19 17:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0029_homevideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homevideo',
            name='home_video',
            field=models.FileField(blank=True, null=True, upload_to='home_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
