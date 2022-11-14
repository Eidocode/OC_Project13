# Generated by Django 3.2.5 on 2022-11-02 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cpu',
            name='smt',
        ),
        migrations.RemoveField(
            model_name='immo',
            name='buy_date',
        ),
        migrations.RemoveField(
            model_name='immo',
            name='cost_center',
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='frequency',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='nb_cores',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='inventory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.inventory'),
        ),
        migrations.AlterField(
            model_name='deviceuser',
            name='first_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='deviceuser',
            name='last_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='immo',
            name='bc_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='addr_mac',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='hostname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='ram',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='serial',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='storage',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='warranty_end',
        ),
        migrations.AlterField(
            model_name='location',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.entity'),
        ),
        migrations.DeleteModel(
            name='Site',
        ),
    ]