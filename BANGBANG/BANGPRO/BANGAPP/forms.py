from django import forms
from .models import User
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