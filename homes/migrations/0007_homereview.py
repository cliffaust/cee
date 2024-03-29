# Generated by Django 3.1 on 2020-09-01 15:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homes', '0006_auto_20200831_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='homes.home')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
