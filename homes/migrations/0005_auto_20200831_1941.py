# Generated by Django 3.1 on 2020-08-31 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0004_home_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opendatetime',
            name='open_date',
            field=models.CharField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=2, max_length=1),
            preserve_default=False,
        ),
    ]
