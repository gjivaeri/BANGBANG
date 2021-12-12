# Generated by Django 2.2 on 2021-12-11 15:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0038_auto_20211212_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='WriterID2',
            field=models.ForeignKey(db_column='test3', default='asfd', on_delete=django.db.models.deletion.CASCADE, related_name='test3', to='BANGAPP.User'),
        ),
        migrations.AlterField(
            model_name='test',
            name='WDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 12, 0, 39, 0, 813951)),
        ),
    ]
