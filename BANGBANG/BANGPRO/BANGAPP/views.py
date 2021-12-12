from django.contrib import auth
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import User, Shop, Shoprev, Theme, ThemeRev, Like, Hate, Test
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#for loginview
from .forms import LoginForm, ThemeRevForm, TestForm
from django.views import generic
from argon2 import PasswordHasher, exceptions
#for likeview
from django.utils.decorators import method_decorator
from .decorator import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView, View, RedirectView #Generic View 개발 속도를 빠르게 만들어줌
from django.views.decorators.csrf import csrf_exempt
#for sort 
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.
def join(request):
    if request.method == 'GET':
        return render(request, 'registration/join.html')
    elif request.method == 'POST':
        userID = request.POST.get('userID', '')
        userPW = request.POST.get('userPW1', '')
        userName = request.POST.get('userName', '')
        usersSubname = request.POST.get('usersSubname', '')
        userBirthday =request.POST.get('userBirthday', '')
        userGender = request.POST.get('userGender')

        if (userID or userPW or userName or usersSubname or userBirthday or userGender) == '':
            return render(request,'registration/join.html')
        elif request.POST['userPW1'] != request.POST['userPW2']:
            return render(request,'registration/join.html')
        else:
            user = User(
              userID = userID,
              userPW = PasswordHasher().hash(userPW),
              userName = userName,
              usersSubname = usersSubname,
              userBirthday = userBirthday,
              userGender = userGender
          )
            user.save()
        return render(request, 'registration/complete.html')


class LoginView(generic.View): 
  template_name = 'registration/login.html'
  form_class = LoginForm
  success_url = reverse_lazy("home") 
  #Class-level 속성을 가지는 객체들은 import 될 때 배치되는데 URL-seolving 규칙은 import 시간에 세팅되어있지 않아 class 내에서 reverse()를 사용하면 URLconf의 규칙을 인식하지 못한다.

  loginform = LoginForm()
  context = { 'forms' : loginform }

  def post(self, request):
      loginform = LoginForm(request.POST)
      context = { 'forms' : loginform }
      if loginform.is_valid():
          print(request.user)
          self.request.session['user'] = loginform.cleaned_data['userID']
          username = self.request.session['user']
          # return super().form_valid(form)
          return render(request, './home.html', {'username' : username})

      else:
          context['forms'] = loginform
          if loginform.errors:
            for value in loginform.errors.values():
                context['error'] = value
      return render(request, 'registration/login.html', context)

  def get(self,request):
      return render(request, 'registration/login.html', context=self.context)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('home')


def mypage(request):
    username = request.session.get('user')
    if User.objects.filter(userID = username).exists():
        content = {'username' : username}
        return render(request, 'registration/mypage.html', content)
    return redirect('login')

    
def home(request):
    shop_list = Shop.objects.all()
    theme_list = Theme.objects.all()
    shopscount = shop_list.count()
    themescount = theme_list.count()
    allcount = shopscount + themescount
    q = request.GET.get('q','')

    if q :
      theme_list = theme_list.filter(themeName__icontains=q)
      shop_list = shop_list.filter(shopName__icontains=q)
      allcount = theme_list.count() + shop_list.count()
    content = {'shop_list' : shop_list, 'theme_list' : theme_list, 'allcount' : allcount, 'q' : q}
    return render(request, 'home.html', content)


def detail_shop(request, shop_pk):
      shop = Shop.objects.get(pk=shop_pk)
      themes = Theme.objects.filter(ShopID=shop_pk)
      review = ThemeRev.objects.filter(theme_ID=shop_pk)
      topreview = review.order_by('-themeRevRecom').first()

      return render(request,'detail_shop.html', {'shop':shop, 'themes':themes, 'review':review, 'topreview':topreview})


def detail_theme(request, theme_pk):
  #이 페이지에서 새로 뭘 작성할게 아니면 아래 두줄은 삭제
    if request.method == "POST":
      return redirect('detail_theme', theme_pk)

    theme = Theme.objects.get(pk=theme_pk)
    review = ThemeRev.objects.filter(theme_ID=theme_pk)
    topreview = review.order_by('-themeRevRecom').first()
    # like = Like.objects.filter(article__in=review)
    return render(request, 'detail_theme.html', {'theme':theme, 'review':review, 'topreview':topreview})
    

def detail_themeRevAdd(request, theme_pk):
  theme = Theme.objects.get(pk=theme_pk)
  reviews = ThemeRev.objects.filter(theme_ID=theme_pk)
  shops = Shop.objects.all()
  return render(request, 'detail_themeRevAdd.html', {'theme':theme ,'reviews': reviews, 'shops':shops})


def detail_themeRevAddDetail(request, theme_pk, review_pk):
  theme = Theme.objects.get(pk=theme_pk)
  review = ThemeRev.objects.get(pk=review_pk)
  shops = Shop.objects.all()
  context = {'theme':theme, 'review':review, 'shops':shops}
  return render(request, 'detail_themeRevAddDetail.html', context)


# 테스트용뷰
def new_themeRevTest(request):
  username = request.session.get('user')
  user = get_object_or_404(User, userID = username)
  if request.method == "POST":
    form = TestForm(request.POST)

    if form.is_valid():
      print(form.cleaned_data)
      post = form.save()
      post.WriterID2 = user
      post.save()
      return redirect("new_themeRevTest")
    else:
      print('no')
  else:
      form = TestForm()
  context = {'form':form}
  return render(request, "new_themeRevTest.html", context)


@csrf_exempt
def selectImg(request):
    pk = request.POST.get('pk', None)
    # username = request.session.get('user')
    # user = get_object_or_404(User, userID = username)
    selectTheme = get_object_or_404(Theme, pk=pk)
    themeImg = selectTheme.themeImage
    return HttpResponse(json.dumps(str(themeImg)), content_type="application/json")


def new_themeRev(request):
  username = request.session.get('user')
  user = get_object_or_404(User, userID = username)
  
  if request.method == "GET":
    form = ThemeRevForm()

  elif request.method == "POST":
    form = ThemeRevForm(request.POST)

    if form.is_valid():
      print(form.cleaned_data)
      post = form.save(commit=False) #DB save를 지연시켜 중복 save 방지
      post.themeRev_WriterID = user
      post.save()
      pk = post.pk
      # return render(request, "new_themeRevCom.html")
      return redirect("detail_themeRev", pk)
    else:
      messages.error(request, 'Error!')
      print('no')
      # post.ip = request.META['REMOTE_ADDR']
      
  context = {'form':form,}
  return render(request, "new_themeRev.html", context)


def edit_themeRev(request, themeRev_pk):
    username = request.session.get('user')
    user = get_object_or_404(User, userID = username)
    themeRev = get_object_or_404(ThemeRev, pk = themeRev_pk)
    # path-converter로 받은 pk로 수정하려는 post객체를 get

    if request.method == "GET":
      form = ThemeRevForm(instance = themeRev)

    elif request.method == "POST":
        form = ThemeRevForm(request.POST, instance=themeRev)
        # ThemeRevForm의 인스턴스가 themeRev임을 표시
        if form.is_valid():
          print(form.cleaned_data)
          post = form.save(commit=False) #DB save를 지연시켜 중복 save 방지
          post.themeRev_WriterID = user
          post.save()
          # return render(request, "new_themeRevCom.html")
          return redirect("detail_themeRev", themeRev_pk=post.pk)
        else:
          messages.error(request, 'Error!')
          print('no')
    context = {'form':form}
    return render(request, 'edit_themeRev.html', context)


def delete_themeRev(request, themeRev_pk):
    themeRev = ThemeRev.objects.get(pk=themeRev_pk)
    themeRev.delete()
    return redirect('list_themeRevAll')


def detail_themeRev(request, themeRev_pk):
    reviews = ThemeRev.objects.all()
    themeRev = ThemeRev.objects.get(pk=themeRev_pk)
    theme = Theme.objects.get(themeName=themeRev.theme_ID)
    writer = User.objects.get(userID=themeRev.themeRev_WriterID)
    # writeDate = themeRev.themeRevWriteDate()
    if request.method == "POST":
        return redirect('detail_themeRev', themeRev_pk)

    return render(request, 'detail_themeRev.html', {'reviews':reviews, 'themeRev': themeRev, 'theme': theme, 'writer': writer})


def list_themeRev(request):
    ordering_priority = []
    order = '' if request.GET.get('order') == 'asc' else '-'
    # 이곳에서 오름차순인지 내림차순인지 알아낸 뒤에 명령어를 변수에 입력해둔다.
    # ?order=asc 라는 string이 있으면 order가 ''가 되어버려서 내림차순으로 정렬되어버림

    # 종합해서 ordering query를 생성한다.
    if request.GET.get('sort') and request.GET.get('sort') != 'themeRevWriteDate':
        # 정렬 기준이 시간이 아닐 때만 해당 값을 ordering_priority에 추가한다.
        # 다른 기준으로 정렬하면 무조건 시간의 내림차순으로 정렬하기 때문에 이런식으로 구성이 된다.
        sort = request.GET.get('sort')
        ordering_priority.append(order + sort)
        ordering_priority.append('-themeRevWriteDate')
    else:
        sort = 'themeRevWriteDate'
        ordering_priority.append(order + sort)

    sorted = ThemeRev.objects.all().order_by(*ordering_priority)
    themes = Theme.objects.all()
    reviews = sorted
    shops = Shop.objects.all()
    users = User.objects.all()
    #차후 구현할 페이지 파트
    paginator = Paginator(sorted,9)
    page = request.GET.get('page','')
    posts = paginator.get_page(page)
    #url에서 page=? 에 들어가는 값. 몇페이지의 정보를 보내는지 알아냄. 공백이어도 허용
    #분할될 객체 / 한페이지에 담길 객체 수
    #페이지 번호를 받아 해당 페이지를 리턴
    
    context = {
      'posts':posts, 'themes':themes, 'sort':sorted, 'reviews':reviews, 'shops':shops, 'users':users
    }
    return render(request,'list_themeRev.html', context)


def list_themeRevAll(request):
  reviews = ThemeRev.objects.all()
  context = {
    'reviews':reviews,
  }
  return render(request, 'list_themeRevAll.html', context)


@csrf_exempt
def like(request):
    pk = request.POST.get('pk', None)
    username = request.session.get('user')
    user = get_object_or_404(User, userID = username)
    article = get_object_or_404(ThemeRev, pk=pk)

    if Like.objects.filter(user=user, article=article).exists():
      Like.objects.filter(user=user, article=article).delete()
      article.themeRevRecom -= 1
      article.save()
      message = '추천 취소'
    else:
      Like(user=user, article=article).save()
      article.themeRevRecom += 1
      article.save()
      message = '추천'
    
    context = {'like_count':article.themeRevRecom, 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def hate(request):
    pk = request.POST.get('pk', None)
    username = request.session.get('user')
    user = get_object_or_404(User, userID = username)
    article = get_object_or_404(ThemeRev, pk=pk)

    if Hate.objects.filter(user=user, article=article).exists():
      Hate.objects.filter(user=user, article=article).delete()
      article.themeRevRecom += 1
      article.save()
      message = '비추천 취소'
    else:
      Hate(user=user, article=article).save()
      article.themeRevRecom -= 1
      article.save()
      message = '비추천'
    
    context = {'like_count':article.themeRevRecom, 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")


def mylike(request):
  username = request.session.get('user')
  user = get_object_or_404(User, userID = username)
  mylikes = Like.objects.filter(user=user)
  #내가 좋아요한(Like) 테마의 이미지(Theme.themeImg)
  #테마리뷰의 like뷰 외에 테마의 like뷰를 만들어야 함

  return render(request, 'mypage/mylike.html')


def recommend(request):
    username = request.session.get('user')
    user = User.objects.filter(userID = username).values('userID')
    themes = Theme.objects.all()
    shops = Shop.objects.all()
    content = {'user' : user, 'themes' : themes, 'shops' : shops}
    return render(request, 'recommend.html', content)
    

def edit_profile(request):
    username = request.session.get('user') # 로그인 해야
    if User.objects.filter(userID = username).exists():
        user = User.objects.get(userID = username)
        content = {
            'username' : username,
            'user' : user
        }
        if request.method == "POST":
            verify = False # 현재 비밀번호가 올바른지 확인
            try:
                PasswordHasher().verify(user.userPW, request.POST.get('userPW', ''))
            except exceptions.VerifyMismatchError:
                verify = False
            else:
                verify = True

            if request.POST.get('userName', '') == '': #이름이 없는 경우
                content['error'] = '이름을 입력해주세요.'
            elif request.POST.get('usersSubname', '') == '': #닉네임이 없는 경우
                content['error'] = '닉네임을 입력해주세요.'  
            elif request.POST.get('userPW', '') == '': # 현재 비밀번호 칸이 비었을 때
                content['error'] = '현재 비밀번호를 입력해주세요.' 
            elif not verify: # 현재 비밀번호가 올바른지
                content['error'] = '현재 비밀번호가 올바르지 않습니다.' 
            elif request.POST.get('userPW1', '') != request.POST.get('userPW2', ''): # 새 비밀번호 확인이 맞는지
                content['error'] = '새 비밀번호 확인이 올바르지 않습니다.' 
            elif request.POST.get('userPW', '') == request.POST.get('userPW1', ''): # 새 비밀번호가 이전 비밀 번호와 같은지
                content['error'] = '이전 비밀번호와 동일 합니다.' 
            else:
                loginform = LoginForm(request.POST)
                if loginform.is_valid():
                    user.userName = request.POST.get('userName', '')
                    if request.POST.get('userPW1', '') != '':
                        user.userPW = PasswordHasher().hash(request.POST.get('userPW1', ''))
                    user.usersSubname = request.POST.get('usersSubname', '')
                    user.userBirthday = request.POST.get('userBirthday', '')
                    user.userGender = int(request.POST.get('userGender', ''))
                    user.save()
                    user.userBirthday = datetime.strptime(user.userBirthday, "%Y-%m-%d")
                    content['user'] = user # 수정된 정보로 업데이트
                    content['message'] = '회원정보가 수정되었습니다.'
                else:
                    content['error'] = '새 비밀번호를 확인해 주세요.' # 새비번 확인이 안 맞았을 때
        return render(request, 'registration/edit_profile.html', content)
    return redirect('login')
