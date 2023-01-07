# Generated by Django 3.2.5 on 2023-01-06 10:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_device_added_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='deviceuser',
            name='email',
            field=models.EmailField(max_length=70, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 10, 20, 23, 380692, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='deviceuser',
            name='assignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.assignment'),
        ),
        migrations.AddField(
            model_name='deviceuser',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.status'),
        ),
    ]
