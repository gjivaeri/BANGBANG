# Generated by Django 2.2 on 2021-11-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BANGAPP', '0016_auto_20211112_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userImage',
            field=models.ImageField(blank=True, upload_to='userImages/'),
        ),
    ]
