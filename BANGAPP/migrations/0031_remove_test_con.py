# Generated by Django 2.2 on 2021-12-08 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0030_auto_20211209_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='con',
        ),
    ]