# Generated by Django 3.1 on 2020-09-19 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0028_home_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_video', models.FileField(blank=True, null=True, upload_to='home_videos')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_videos', to='homes.home')),
            ],
        ),
    ]