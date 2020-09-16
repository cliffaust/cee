# Generated by Django 3.1 on 2020-09-11 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0022_auto_20200911_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralHomeFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_feature', models.CharField(blank=True, max_length=60, null=True)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general_home_features', to='homes.home')),
            ],
        ),
    ]
