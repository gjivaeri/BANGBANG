# (멋사 프로젝트2차) 방탈출 리뷰 사이트 BANGBANG
방탈출 관련 리뷰들을 모아볼 수 있는 사이트 <br>
실행 전에 관련 라이브러리 설치를 필요로 합니다. (Installation 참고)

## 서비스 설명
## 주요기능
## 기술스택
## 실행화면

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries

```bash
pipenv shell
pipenv install django
pip install pillow
pip install argon2-cffi
```

if error occurs, please migrate dummy data before runserver
```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage
### **(+보충)pillow 사용법 적어주세요**

```python
from argon2 import PasswordHasher, exceptions
from pillow?

# hash user's password in views.py
user = User(
  userID = userID,
  userPW = PasswordHasher().hash(userPW),
)
..
if request.POST.get('userPW1', '') != '':
    user.userPW = PasswordHasher().hash(request.POST.get('userPW1', ''))

# PHP function to check hashed password in forms.py
try:
    PasswordHasher().verify(user.userPW, userPW)
except exceptions.VerifyMismatchError:
    return self.add_error('userPW', '비밀번호가 다릅니다')

```

## License
[MIT](https://choosealicense.com/licenses/mit/)
