# Generated by Django 2.2 on 2021-11-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0014_auto_20211112_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='themeRating',
            new_name='score',
        ),
    ]
