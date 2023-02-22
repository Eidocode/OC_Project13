# Generated by Django 3.2.5 on 2023-02-08 18:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_device_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 8, 18, 14, 24, 540403, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.deviceuser'),
        ),
        migrations.AlterField(
            model_name='device',
            name='immo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.immo'),
        ),
    ]