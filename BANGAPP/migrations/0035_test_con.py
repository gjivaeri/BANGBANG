# Generated by Django 2.2 on 2021-12-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0034_remove_test_con'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='con',
            field=models.TextField(null=True),
        ),
    ]
