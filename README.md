# 🦁멋사 프로젝트2차🦁 방탈출 리뷰 사이트 BANGBANG
방탈출 관련 리뷰들을 모아볼 수 있는 사이트 <br>
실행 전에 관련 라이브러리 설치를 필요로 합니다. (하단 Installation 참고)

[디자인시안](https://xd.adobe.com/view/e0e54edb-2c9c-41ce-8a15-2a08127117c6-b5b6/screen/284d5790-8455-4732-8176-7b9fa7c5a715/)

## 📖서비스 설명
방탈출 카페 시장규모가 커짐에 따라, 다양하게 즐길 수 있는 동시에 불편함도 존재했습니다. <br>
온라인은 하나의 공식 홈페이지에서 관리하는 것이 아니라 각 매장별 홈페이지가 있었기 때문입니다.

- 문제점 
1. 비교를 원할 때에도 일일이 확인을 해야 하는 번거로움 
2. 400여개의 매장과 1737개의 다양한 테마로 정보탐색의 어려움 
3. 매장 별로 제공된 난이도와 공포도는 개인차가 존재 
- 해결방안
1. 모든 매장과 테마를 한 사이트에서 모아서 비교
2. 별점/위치/난이도 등 필터 설정하여 쉽게 정보 탐색 가능 
3. 한 눈에 볼 수 있는 댓글 형태 리뷰 맞춤화 서비스까지 제공 

'빙방이' 서비스는 이러한 문제점을 모두 해결해 주는 방탈출 카페 플랫폼입니다.

## 📚주요기능
1. 방탈출 테마, 가게별 테마, 테마 리뷰 모아보기 기능
3. 테마 검색 및 필터링 기능
4. 인기순, 가격순 테마 정렬 기능
5. 특정 태그에 따른 테마 추천 및 모아보기 기능
6. session을 이용한 회원가입 및 마이페이지 회원정보 수정
7. 프로필 이미지 업로드 기능
8. 방탈출 테마 리뷰 작성 및 별점 기능
9. 테마 및 테마 리뷰 좋아요 기능
10. 내가 작성한 리뷰, 좋아요 한 테마 모아보기 기능

## ⚙️기술스택

| FRONT-END          | BACK-END               |
| ----------------- |:----------------------- |
| HTML, CSS, Jquery(+ajax)       | Django   |
## 💻실행화면
+ 테마 검색<br>
![1 검색](https://user-images.githubusercontent.com/66814071/146974086-9230b25b-4df4-463e-bd6a-7126168f7cb5.gif)
  + GET 메서드를 받아와 테마 검색 기능 구현
  + js기반 좋아요순, 가격순 필터링 구현
+ 테마 상세 및 좋아요, 예약 페이지 (예약페이지는 추후 구현)<br>
![2 테마상세](https://user-images.githubusercontent.com/66814071/146974158-79ff55ae-cad1-4b8b-afb8-98762206790e.gif)
  + 테마별 리뷰 모아보기 및 좋아요 기능 (ajax를 이용한 동적구현)
  + 내가 작성한 리뷰만 수정/삭제 기능 (리뷰모델의 작성자와 로그인유저 비교, forms.py 에서 기존 데이터 불러오기)
+ 테마 추천<br>
![3 추천](https://user-images.githubusercontent.com/66814071/146974192-d50acf0c-d550-4474-986a-72245ecfe765.gif)
  + 태그별 추천 테마 제공 
+ 리뷰 목록<br>
![4 리뷰목록gif](https://user-images.githubusercontent.com/66814071/146974215-26b62223-24fe-483e-b26b-01c64a883730.gif)
  + 작성된 테마 리뷰 모아보기 기능
  + 최신순, 좋아요순, 별점순 정렬기능 (jquery) 
+ 새 리뷰 작성 및 별점 부여 기능<br>
![5 리뷰작성](https://user-images.githubusercontent.com/66814071/146974260-3fe855ae-6084-4015-a1af-6794754653e4.gif)
  + jquery 기반 동적 이미지 불러오기
  + 날짜 선택을 위한 datepicker 라이브러리
  + 별점 이미지-점수 연동을 위한 rate-it plugin
  + 관리자 페이지 별점 확인을 위한 widget구현
+ 마이페이지<br>
![6 회원정보수정](https://user-images.githubusercontent.com/66814071/146974405-8807335c-50cf-4213-ab2b-89236c71a5f6.gif)
  + 로그인 유저에게만 접근 권한 부여
  + 회원정보 수정 및 프로필 사진 업로드
  + session을 이용한 회원가입 (비밀번호 암호화를 위해 argon2 암호화툴 사용)
+ 리뷰관리<br>
![7 리뷰관리](https://user-images.githubusercontent.com/66814071/146974464-d6c71714-f905-4e10-8b95-3e4d91163d14.gif)
  + 내 좋아요 모아보기
  + 내 작성 리뷰 모아보기

## 🧰Installation

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
