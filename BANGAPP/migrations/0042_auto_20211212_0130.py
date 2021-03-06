# Generated by Django 2.2 on 2021-12-11 16:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0041_auto_20211212_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='WDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 12, 1, 30, 8, 44758)),
        ),
        migrations.AlterField(
            model_name='themerev',
            name='themeRevNRecom',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='themerev',
            name='themeRevRecom',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='themerev',
            name='themeRevWriteDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 12, 1, 30, 8, 43995)),
        ),
        migrations.AlterField(
            model_name='themerev',
            name='themeRev_WriterID',
            field=models.ForeignKey(blank=True, db_column='themeRev_WriterID', on_delete=django.db.models.deletion.CASCADE, related_name='themeRev_WriterID', to='BANGAPP.User'),
        ),
    ]
