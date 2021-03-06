# Generated by Django 3.2.7 on 2021-10-02 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shopID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('shopName', models.CharField(max_length=200)),
                ('Location', models.TextField()),
                ('OpenTime', models.TextField()),
                ('Rating', models.IntegerField(default=0)),
                ('Difficulty', models.IntegerField(default=0)),
                ('Horror', models.IntegerField(default=0)),
                ('PhoneNum', models.CharField(max_length=200)),
                ('Price', models.IntegerField(default=0)),
                ('PageLink', models.TextField()),
                ('ShopIntro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('themeID', models.IntegerField(primary_key=True, serialize=False)),
                ('themeName', models.CharField(max_length=128)),
                ('themeTimeLimit', models.CharField(max_length=64)),
                ('themeRating', models.IntegerField(default=0)),
                ('themeDifficulty', models.IntegerField(default=0)),
                ('themeHorror', models.IntegerField(default=0)),
                ('themeActivity', models.IntegerField(default=0)),
                ('themeRecomPeople', models.IntegerField()),
                ('themeGenre', models.CharField(max_length=64)),
                ('ShopID', models.ForeignKey(db_column='ShopID', on_delete=django.db.models.deletion.CASCADE, related_name='ShopId', to='BANGAPP.shop')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('userPW', models.CharField(max_length=128)),
                ('userName', models.CharField(max_length=64)),
                ('usersSubname', models.CharField(max_length=64)),
                ('userBirthday', models.DateField()),
                ('userGender', models.IntegerField(default=0)),
                ('ShopRevID', models.IntegerField(default=0)),
                ('ThRevID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeRev',
            fields=[
                ('themeRevID', models.IntegerField(primary_key=True, serialize=False)),
                ('themeRevTitle', models.CharField(max_length=200)),
                ('themeRevRating', models.IntegerField(default=0)),
                ('themeRevDifficulty', models.IntegerField(default=0)),
                ('themeRevHorror', models.IntegerField(default=0)),
                ('themeRevActivity', models.IntegerField(default=0)),
                ('themeRevContent', models.TextField()),
                ('themeRevImage', models.ImageField(upload_to=None)),
                ('themeRevResult', models.BooleanField(null=True)),
                ('themeRevOccurredTime', models.TimeField()),
                ('themeRevDate', models.DateField()),
                ('themeRevWriteDate', models.DateTimeField(auto_now_add=True)),
                ('ResID', models.IntegerField()),
                ('themeRevRecom', models.IntegerField()),
                ('themeRevNRecom', models.IntegerField()),
                ('themeRev_WriterID', models.ForeignKey(db_column='themeRev_WriterID', on_delete=django.db.models.deletion.CASCADE, related_name='themeRev_WriterID', to='BANGAPP.user')),
                ('theme_ID', models.ForeignKey(db_column='theme_id', on_delete=django.db.models.deletion.CASCADE, related_name='theme_ID', to='BANGAPP.theme')),
            ],
        ),
        migrations.CreateModel(
            name='Shoprev',
            fields=[
                ('shoprevID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('shoprevTitle', models.CharField(max_length=200)),
                ('shopRating', models.IntegerField(default=0)),
                ('shoprevCont', models.TextField()),
                ('shoprevImage', models.ImageField(upload_to='')),
                ('shoprevDate', models.DateField()),
                ('shoprevWDate', models.DateField(auto_now=True)),
                ('recom', models.IntegerField(default=0)),
                ('nrecom', models.IntegerField(default=0)),
                ('WriterID', models.ForeignKey(db_column='WriterID', on_delete=django.db.models.deletion.CASCADE, related_name='UserID', to='BANGAPP.user')),
                ('shopID', models.ForeignKey(db_column='shopID', on_delete=django.db.models.deletion.CASCADE, related_name='ShopID', to='BANGAPP.shop')),
            ],
        ),
    ]
