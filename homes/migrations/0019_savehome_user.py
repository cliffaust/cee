# Generated by Django 3.1 on 2020-09-05 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homes', '0018_auto_20200905_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='savehome',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.customuser'),
            preserve_default=False,
        ),
    ]
