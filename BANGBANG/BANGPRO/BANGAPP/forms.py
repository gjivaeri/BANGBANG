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
    # fields = ('themeRevContent', 'themeRevDate', 'themeRev_WriterID', 'theme_ID', 'shop_ID', 'themeRevRating')
    widgets = {
      'themeRevDate': forms.DateInput(attrs={'class':'datepicker', 'id':'date'}),
      'theme_ID': forms.Select(attrs={'name':'theme', 'onchange':'changeTheme()'}),
      # 'theme_ID': forms.Select(attrs={'name':'theme', 'onchange':'changeTheme()', 'class':'visitedTheme'}),
      # 'shop_ID': forms.NullBooleanSelect(attrs={'id':'shopid'}),
      'themeRevRating': starWidget,
    }


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        js = ('js/new_themeRev.js',)
        # js = ('js/new_themeRev.js',)
        widgets = {
            # 'grade': starWidget(attrs={'name':'grade','id':'star_id_grade'}),
            'grade': starWidget,
            'Date': forms.DateInput(attrs={'class':'datepicker'}),
        }