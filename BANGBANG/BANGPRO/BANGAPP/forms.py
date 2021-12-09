from enum import auto
from django import forms
from django.forms import ModelForm
from .models import User, Theme, ThemeRev, Test
from argon2 import PasswordHasher, exceptions
from .widgets import starWidget

class LoginForm(forms.Form):
  userID = forms.CharField(
    max_length=32,
    label='userID',
    required=True,
    widget=forms.TextInput(
        attrs={
          'class' : 'userID',
          'placeholder' : '아이디를 입력해주세요'
        }
    ),
    error_messages={'requred' : '아이디를 입력하세요'}
  )
  userPW = forms.CharField(
      max_length=32,
      label='userPW',
      required=True,
      widget=forms.PasswordInput(
          attrs={
                'class' : 'userPW',
                'placeholder' : '비밀번호를 입력해주세요'
          }
      ),
      error_messages={'requred' : '비밀번호를 입력하세요'}
  )

  field_order = [
    'userID',
    'userPW',
  ]

  def clean(self):
    cleaned_data = super().clean()
    userID = cleaned_data.get('userID')
    userPW = cleaned_data.get('userPW')

    if userID and userPW:
        try:
            user = User.objects.get(userID=userID)
        except User.DoesNotExist:
            self.add_error('userID', '아이디가 존재하지 않습니다')
            return
        try:
            PasswordHasher().verify(user.userPW, userPW)
        except exceptions.VerifyMismatchError:
            return self.add_error('userPW', '비밀번호가 다릅니다')
        else:
            self.userID = user.userID

class ThemeRevForm(ModelForm):
  class Meta:
    model = ThemeRev
    fields = '__all__'
    js = ('js/new_themeRev.js',)
    # fields = ('themeRevTitle', 'themeRevContent', 'themeRevDate', 'themeRev_WriterID', 'theme_ID', 'shop_ID', 'themeRevRating')
    widgets = {
      'themeRevDate': forms.DateInput(attrs={'class':'datepicker'}),
      'theme_ID': forms.NullBooleanSelect(attrs={'name':'theme', 'onchange':'changeTheme()', 'class':'visitedTheme', 'default':'1'}),
      'themeRevRating': starWidget,
    }

    
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        js = ('js/new_themeRev.js',)
        widgets = {
            # 'grade': starWidget(attrs={'id':'star_id_grade','class':'rateit rateit-bg','data-rateit-backingfld':'#id_grade'}),
            'grade': starWidget(attrs={'name':'grade'}),
        }
        
    # <input type="rating" name="grade" value="4" required="" id="id_grade" min="0" max="5" step="1" style="display: none;">
    # <div id="star_id_grade" class="rateit rateit-bg" data-rateit-backingfld="#id_grade">




#     themeRevID = models.AutoField(primary_key=True)
#     themeRevTitle = models.CharField(max_length=200)
#     themeRevContent = models.TextField()
#     themeRevDate = models.DateField()
#     themeRevWriteDate = models.DateTimeField(auto_now_add=True)
#     themeRev_WriterID = models.ForeignKey("User", related_name="themeRev_WriterID", on_delete=models.CASCADE, db_column="themeRev_WriterID")
#     theme_ID = models.ForeignKey("Theme", related_name="theme_ID", on_delete=models.CASCADE, db_column="theme_id")
#     shop_ID = models.ForeignKey("Shop", related_name="shop_ID", on_delete=models.CASCADE, db_column="shop_id", default=1)
#     themeRevRecom = models.IntegerField(default=0)
#     themeRevNRecom = models.IntegerField(default=0) {% endcomment %}

  
  # class Meta:
    # model = Theme
    # fields = ('themeImage', 'themeName', 'themeRating')

  # class Meta:
  #   model = User
  #   fields = ('usersSubname, userImage')

  # class Meta:
  #   model = Shop
  #   fields = ('shopName')
    # fields = ['themeRevTitle']
# class ThemeRevWrite(forms.Form):
#   class Meta:
#       model = ThemeRev

#       fields = ['themeRevTitle', '']

#       theme = forms.ModelChoiceField(queryset=Theme.objects.all()) # Or whatever query you'd like
