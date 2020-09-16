# Generated by Django 3.1 on 2020-09-02 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0009_auto_20200902_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.IntegerField(blank=True)),
                ('latitude', models.IntegerField(blank=True)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_coordinate', to='homes.home')),
            ],
        ),
        migrations.DeleteModel(
            name='HomeLocation',
        ),
    ]