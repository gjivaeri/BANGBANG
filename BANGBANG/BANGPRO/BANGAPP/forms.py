from enum import auto
from django import forms
from .models import User, Theme, ThemeRev
from argon2 import PasswordHasher, exceptions


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

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

# class ThemeRevWrite(forms.Form):
#   class Meta:
#       model = ThemeRev

#       fields = ['themeRevTitle', '']

#       theme = forms.ModelChoiceField(queryset=Theme.objects.all()) # Or whatever query you'd like

# (유저의)이미지 /자동
# (유저의)이름 /자동
# (테마리뷰의)themeRevWriteDate /자동
# (테마의)별점, 
# (테마의)이미지,
# (테마의)이름,
# (가게의)이름,
# (테마리뷰의)themeRevDate,
# (테마리뷰의)themeRevContent

# themeRevID = models.AutoField(primary_key=True)
# themeRevContent = models.TextField()
# themeRevDate = models.DateField()
# themeRevWriteDate = models.DateTimeField(auto_now_add=True)
# theme_ID = models.ForeignKey("Theme", related_name="theme_ID", on_delete=models.CASCADE, db_column="theme_id")
# themeRevRecom = models.IntegerField(default=0)
# themeRevNRecom = models.IntegerField(default=0)
# themeRev_WriterID = models.ForeignKey("User", related_name="themeRev_WriterID", on_delete=models.CASCADE, db_column="themeRev_WriterID")
    