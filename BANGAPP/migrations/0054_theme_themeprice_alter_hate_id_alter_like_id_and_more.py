# Generated by Django 4.0 on 2021-12-21 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0053_auto_20211215_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='themePrice',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='hate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='test',
            name='WDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 21, 22, 5, 56, 361461)),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='themelike',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='themerev',
            name='themeRevWriteDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 21, 22, 5, 56, 360453)),
        ),
    ]