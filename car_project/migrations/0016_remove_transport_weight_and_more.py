# Generated by Django 4.1.6 on 2023-04-18 20:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_project', '0015_remove_check_in_out_resident_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='transporttype',
            name='max_weight',
        ),
        migrations.RemoveField(
            model_name='transporttype',
            name='min_weight',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.TextField(blank=True, default='Не исполнен'),
        ),
        migrations.AddField(
            model_name='transport',
            name='width',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transporttype',
            name='max_width',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transporttype',
            name='min_width',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resident',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resident',
            name='passport',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]