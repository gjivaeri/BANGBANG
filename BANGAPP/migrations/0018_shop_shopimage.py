# Generated by Django 2.2 on 2021-11-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0017_user_userimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shopImage',
            field=models.ImageField(blank=True, upload_to='shopImages/'),
        ),
    ]
