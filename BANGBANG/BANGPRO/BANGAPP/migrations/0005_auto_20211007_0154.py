# Generated by Django 2.2 on 2021-10-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0004_auto_20211002_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoprev',
            name='shoprevImage',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='themerev',
            name='themeRevImage',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]