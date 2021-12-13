from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime    

# Create your models here.

class User(models.Model):
    userID = models.CharField(primary_key=True, max_length=128, unique=True)
    userPW = models.CharField(max_length=128)
    userName = models.CharField(max_length=64)
    usersSubname = models.CharField(max_length=64)
    userBirthday = models.DateField()
    userGender = models.IntegerField(default=0)
    ShopRevID = models.IntegerField(default=0)
    ThRevID = models.IntegerField(default=0)
    userImage = models.ImageField(upload_to='userImages/', height_field=None, width_field=None,blank=True, default='userImages/defalut.svg')    

    def __str__(self):
        return self.usersSubname


class Shoprev(models.Model):
    shoprevID = models.AutoField(primary_key=True, unique=True)
    shoprevTitle = models.CharField(max_length=200)
    shopRating = models.IntegerField(default=0)
    shoprevCont = models.TextField()
    shoprevImage = models.ImageField(upload_to='shopImages', height_field=None, width_field=None,blank=True)
    shoprevDate = models.DateField()
    shoprevWDate = models.DateField(auto_now=True)
    shopID = models.ForeignKey("Shop", related_name="ShopID", on_delete=models.CASCADE, db_column='shopID')
    recom = models.IntegerField(default=0)
    nrecom = models.IntegerField(default=0)
    WriterID = models.ForeignKey("User", related_name="UserID", on_delete=models.CASCADE, db_column='WriterID')

    def __str__(self):
        return self.shoprevTitle


class Shop(models.Model):
    shopID = models.AutoField(primary_key=True, unique=True)
    shopName = models.CharField(max_length=200)
    Location = models.TextField()
    OpenTime = models.TextField()
    Rating = models.IntegerField(default=0)
    PhoneNum = models.CharField(max_length=200)
    Price = models.IntegerField(default=0)
    PageLink = models.TextField()
    ShopIntro = models.TextField()
    shopImage = models.ImageField(upload_to='shopImages/', height_field=None, width_field=None,blank=True)    

    def __str__(self):
      return self.shopName


class ThemeRev(models.Model):
    themeRevID = models.AutoField(primary_key=True)
    themeRevContent = models.TextField()
    themeRevDate = models.DateField()
    themeRevWriteDate = models.DateTimeField(default=datetime.now(), blank=True)
    themeRev_WriterID = models.ForeignKey("User", related_name="themeRev_WriterID", on_delete=models.DO_NOTHING, db_column="themeRev_WriterID", blank=True)
    theme_ID = models.ForeignKey("Theme", related_name="theme_ID", on_delete=models.CASCADE, db_column="theme_id")
    shop_ID = models.ForeignKey("Shop", related_name="shop_ID", on_delete=models.CASCADE, db_column="shop_id")
    themeRevRecom = models.IntegerField(default=0, blank=True)
    themeRevNRecom = models.IntegerField(default=0, blank=True)
    themeRevRating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Theme(models.Model):
    themeID = models.AutoField(primary_key=True, unique=True)
    themeName = models.CharField(max_length=128)
    themeTimeLimit = models.CharField(max_length=64)
    themeRating = models.IntegerField(default=0)
    themeDifficulty = models.IntegerField(default=0)
    themeHorror = models.IntegerField(default=0)
    themeActivity = models.IntegerField(default=0)
    themeRecomPeople = models.IntegerField()
    ShopID = models.ForeignKey("Shop", related_name="ShopId", on_delete=models.CASCADE, db_column="ShopID", default=1)
    themeGenre = models.CharField(max_length=64)
    themeImage = models.ImageField(upload_to='themeImages/', height_field=None, width_field=None,blank=True)    
    themeIntro = models.TextField(null=True)
    themeLike = models.IntegerField(default=0, blank=True)

    def __str__(self):
      return self.themeName


class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="like_record")
    article = models.ForeignKey('ThemeRev', on_delete=models.CASCADE, related_name="like_record")
    
    class Meta:
        unique_together = ('user','article')

class Hate(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="hate_record")
    article = models.ForeignKey('ThemeRev', on_delete=models.CASCADE, related_name="hate_record")
    
    class Meta:
        unique_together = ('user','article')


class ThemeLike(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="themelike_record")
    liketheme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name="themelike_record")
    
    class Meta:
        unique_together = ('user','liketheme')


class Test(models.Model):
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    con = models.TextField(null=True)
    Date = models.DateField(null=True)
    WDate = models.DateTimeField(default=datetime.now(), blank=True)
    themeRevRecom = models.IntegerField(default=0, blank=True)
    themeRevNRecom = models.IntegerField(default=0, blank=True)
    theme_ID2 = models.ForeignKey("Theme", related_name="test1", on_delete=models.CASCADE, db_column="test1", default=1)
    shop_ID2 = models.ForeignKey("Shop", related_name="test2", on_delete=models.CASCADE, db_column="test2", default=1)
    WriterID2 = models.ForeignKey("User", related_name="test3", on_delete=models.CASCADE, db_column="test3", null=True, blank=True)

    