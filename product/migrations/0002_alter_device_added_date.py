# Generated by Django 3.2.5 on 2023-04-15 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 9, 9, 50, 862988, tzinfo=utc)),
        ),
    ]
