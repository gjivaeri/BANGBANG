from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
    userImage = models.ImageField(upload_to='userImages/', height_field=None, width_field=None,blank=True)    

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


# class ThemeRev(models.Model):
#     themeRevID = models.AutoField(primary_key=True)
#     themeRevTitle = models.CharField(max_length=200)
#     themeRevRating = models.IntegerField(default=0)
#     themeRevDifficulty = models.IntegerField(default=0)
#     themeRevHorror = models.IntegerField(default=0)
#     themeRevActivity = models.IntegerField(default=0)
#     themeRevContent = models.TextField()
#     themeRevImage = models.ImageField(upload_to='themeRevImages', height_field=None, width_field=None,blank=True)    
#     # themeRevImage = models.ImageField(upload_to=None, height_field=None, width_field=None,blank=True)
#     themeRevResult = models.BooleanField(null=True)
#     themeRevOccurredTime = models.TimeField(auto_now=False, auto_now_add=False)
#     themeRevDate = models.DateField()
#     themeRevWriteDate = models.DateTimeField(auto_now_add=True)
#     theme_ID = models.ForeignKey("Theme", related_name="theme_ID", on_delete=models.CASCADE, db_column="theme_id")
#     ResID = models.IntegerField(default=0)
#     themeRevRecom = models.IntegerField(default=0)
#     themeRevNRecom = models.IntegerField(default=0)
#     themeRev_WriterID = models.ForeignKey("User", related_name="themeRev_WriterID", on_delete=models.CASCADE, db_column="themeRev_WriterID")
    
#     def __str__(self):
#         return self.themeRevTitle

class ThemeRev(models.Model):
    themeRevID = models.AutoField(primary_key=True)
    themeRevContent = models.TextField()
    themeRevDate = models.DateField()
    themeRevWriteDate = models.DateTimeField(auto_now_add=True)
    themeRev_WriterID = models.ForeignKey("User", related_name="themeRev_WriterID", on_delete=models.CASCADE, db_column="themeRev_WriterID")
    theme_ID = models.ForeignKey("Theme", related_name="theme_ID", on_delete=models.CASCADE, db_column="theme_id")
    shop_ID = models.ForeignKey("Shop", related_name="shop_ID", on_delete=models.CASCADE, db_column="shop_id", default=1)
    themeRevRecom = models.IntegerField(default=0)
    themeRevNRecom = models.IntegerField(default=0)
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

class Test(models.Model):
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    con = models.TextField(null=True)
