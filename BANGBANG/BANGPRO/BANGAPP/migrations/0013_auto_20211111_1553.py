# Generated by Django 2.2 on 2021-11-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0012_auto_20211110_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='themeImage',
            field=models.ImageField(blank=True, upload_to='themeImages'),
        ),
        migrations.AlterField(
            model_name='themerev',
            name='themeRevImage',
            field=models.ImageField(blank=True, upload_to='themeRevImages'),
        ),
    ]