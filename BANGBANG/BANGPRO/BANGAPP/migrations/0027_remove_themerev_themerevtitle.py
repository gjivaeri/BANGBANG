# Generated by Django 2.2 on 2021-12-08 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0026_auto_20211207_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='themerev',
            name='themeRevTitle',
        ),
    ]
