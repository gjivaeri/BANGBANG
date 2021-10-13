from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import User, Shop, Shoprev, Theme, ThemeRev, Like, Hate
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#for loginview
from .forms import LoginForm
from django.views import generic
from argon2 import PasswordHasher, exceptions
#for likeview
from django.utils.decorators import method_decorator
from .decorator import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, RedirectView #Generic View 개발 속도를 빠르게 만들어줌
#for sort 
from django.core.paginator import Paginator


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


def home(request):
    username = request.session.get('user')
    user = User.objects.filter(userID = username).values('userID')
    content = {'user' : user}
    return render(request, 'home.html', content)


def shop(request, shop_pk):
    shop = Shop.objects.get(pk=shop_pk)
    reviews = Shoprev.objects.filter(shopID=shop_pk)

    return render(request,'shop.html',{'shop':shop, 'reviews':reviews})

def theme(request, theme_pk):
    theme = Theme.objects.get(pk=theme_pk)
    reviews = ThemeRev.objects.filter(theme_ID=theme_pk)

    return render(request, 'theme.html', {'theme': theme, 'reviews' : reviews})

def detail_shopRev(request, shopRev_pk):
    shopRev = Shoprev.objects.get(pk=shopRev_pk)
    if request.method == "POST":
        return redirect('detail_shopRev', shopRev_pk)

    return render(request, 'detail_shopRev.html', {'shopRev': shopRev})

#theme Review
# @login_required(login_url="/registration/login")
def new_themeRev(request):
    username = request.session.get('user')
    if User.objects.filter(userID = username).exists():
      if request.method == "POST":
          new_themeRev = ThemeRev.objects.create(
            themeRevTitle=request.POST["themeRevTitle"],
            themeRevRating=request.POST["themeRevRating"],
            themeRevDifficulty=request.POST["themeRevDifficulty"],
            themeRevHorror=request.POST["themeRevHorror"],
            themeRevActivity=request.POST["themeRevActivity"],
            themeRevContent=request.POST["themeRevContent"],
            themeRevImage=request.POST["themeRevImage"],
            themeRevResult=request.POST["themeRevResult"],
            themeRevOccurredTime=request.POST["themeRevOccurredTime"],
            themeRevDate=request.POST["themeRevDate"],
            #themeRev_WriterID=request.user,
          )
          return redirect("detail_themeRev", new_themeRev.pk)
      return render(request, "new_themeRev.html")
    else:
      return render(request, 'registration/join.html')


def edit_themeRev(request, themeRev_pk):
    themeRev = ThemeRev.objects.get(pk=themeRev_pk)

    if request.method == "POST":
        ThemeRev.objects.filter(pk=themeRev_pk).update(
            themeRevTitle=request.POST["themeRevTitle"],
            themeRevRating=request.POST["themeRevRating"],
            themeRevDifficulty=request.POST["themeRevDifficulty"],
            themeRevHorror=request.POST["themeRevHorror"],
            themeRevActivity=request.POST["themeRevActivity"],
            themeRevContent=request.POST["themeRevContent"],
            themeRevImage=request.POST["themeRevImage"],
            themeRevResult=request.POST["themeRevResult"],
            themeRevOccurredTime=request.POST["themeRevOccurredTime"],
            themeRevDate=request.POST["themeRevDate"],
            themeRevWriteDate=request.POST["themeRevWriteDate"],
            themeRev_WriterID=request.user,
        )
        return redirect('detail_themeRev', themeRev_pk)

    return render(request, 'edit_themeRev.html', {'themeRev': themeRev})


def detail_themeRev(request, themeRev_pk):
    themeRev = ThemeRev.objects.get(pk=themeRev_pk)
    if request.method == "POST":
        return redirect('detail_themeRev', themeRev_pk)

    return render(request, 'detail_themeRev.html', {'themeRev': themeRev})

#SHOP Review
# @login_required(login_url="/registration/login")
def new_shopRev(request):
    username = request.session.get('user')
    if User.objects.filter(userID = username).exists():
      if request.method == "POST":
          new_shopRev = Shoprev.objects.create(
            shopRevTitle=request.POST["shoprevTitle"],
            shopRevRating=request.POST["shopRating"],
            shopRevContent=request.POST["shoprevCont"],
            shopRevImage=request.POST["shoprevImage"],
            shopRevDate=request.POST["shoprevDate"],
            shopRevWriteDate=request.POST["shoprevWDate"],
            shopRev_WriterID=request.user,
          )
          return redirect("detail_shopRev", new_shopRev.pk)
      return render(request, "new_shopRev.html")
    else:
      return render(request, 'registration/join.html')
    

def edit_shopRev(request, shopRev_pk):
    shopRev = Shoprev.objects.get(pk=shopRev_pk)

    if request.method == "POST":
        shopRev.objects.filter(pk=shopRev_pk).update(
           shopRevTitle=request.POST["shopRevTitle"],
           shopRevRating=request.POST["shopRevRating"],
           shopRevContent=request.POST["shopRevContent"],
           shopRevImage=request.POST["shopRevImage"],
           shopRevDate=request.POST["shopRevDate"],
           shopRevWriteDate=request.POST["shopRevWriteDate"],
           shopRev_WriterID=request.user,
        )
        return redirect('detail_shopRev', shopRev_pk)

    return render(request, 'edit_shopRev.html', {'shopRev': shopRev})

def delete_shopRev(request, shopRev_pk):
    shopRev = Shoprev.objects.get(pk=shopRev_pk)
    shopRev.delete()
    return redirect('/shop/<int:shopRev_pk>')


def delete_themeRev(request, themeRev_pk):
    themeRev = ThemeRev.objects.get(pk=themeRev_pk)
    themeRev.delete()
    return redirect('theme')


# class ListThemeRev(View):
#   def sort(request):
#     ordering_priority = []

#     # 이곳에서 오름차순인지 내림차순인지 알아낸 뒤에 명령어를 변수에 입력해둔다.
#     order = '' if request.GET.get('order') == 'asc' else '-'

#     # 종합해서 ordering query를 생성한다.
#     if request.GET.get('sort') and request.GET.get('sort') != 'timestamp':
#         # 정렬 기준이 시간이 아닐 때만 해당 값을 ordering_priority에 추가한다.
#         # 시나리오대로라면 이곳에 like_count라는 값이 들어갔을 것이다.
#         # 다른 기준으로 정렬하면 무조건 시간의 내림차순으로 정렬하기 때문에 이런식으로 구성이 된다.
#         sort = request.GET.get('sort')
#         ordering_priority.append(order + sort)
#         ordering_priority.append('-timestamp')
#     else:
#         sort = 'timestamp'
#         ordering_priority.append(order + sort)
                
#     sorted = ThemeRev.objects.all().order_by(*ordering_priority)

#     paginator = Paginator(sorted,9)
#     #분할될 객체 / 한페이지에 담길 객체 수
#     page = request.GET.get('page','')
#     #url에서 page=? 에 들어가는 값. 몇페이지의 정보를 보내는지 알아냄. 공백이어도 허용
#     posts = paginator.get_page(page)
#     #페이지 번호를 받아 해당 페이지를 리턴
#     themes = Theme.objects.all()
#     reviews = ThemeRev.objects.all()
#     shops = Shop.objects.all()
    
#     return render(request,'home.html',{'posts':posts, 'themes':themes, 'sort':sort, 'reviews':reviews, 'shops':shops})


def list_themeRev(request):
    reviews = ThemeRev.objects.all()
    themes = Theme.objects.all()
    shops = Shop.objects.all()
    return render(request, 'list_themeRev.html', {'shops':shops, 'themes':themes, 'reviews':reviews})


def list_shopRev(request):
    reviews = Shoprev.objects.all()
    shops = Shop.objects.all()
    return render(request, 'list_shopRev.html', {'shops':shops, 'reviews':reviews})


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
      #args는 튜플, kwargs는 사전형을 인자로 받음. 리디렉션할 대상 url를 구성
        return reverse('detail_themeRev', kwargs={'themeRev_pk':kwargs['pk']})
        #reverse(): view 함수를 사용하여 URL을 역으로 계산=url이 변경되어도 pattern name만 알면 됨
        #args와 kwargs를 동시에 전달할 수 없음

    def get(self, *args, **kwargs):
        username = self.request.session.get('user')
        user = get_object_or_404(User, userID = username)
        article = get_object_or_404(ThemeRev, pk=kwargs['pk'])
        #pk가 존재하는 themeRev 있으면 가져오고 아님 404에러발생

        if Like.objects.filter(user=user, article=article).exists():
          Like.objects.filter(user=user, article=article).delete()
          article.themeRevRecom -= 1
          article.save()
          # messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 가능합니다.') 차후구현
          return HttpResponseRedirect(reverse('detail_themeRev', kwargs={'themeRev_pk':kwargs['pk']}))
        else:
          Like(user=user, article=article).save()
          #like 모델이 존재하면 (좋아요를 이미 눌렀으면 error 발생), 아니면 Like모델에 저장

        article.themeRevRecom += 1
        article.save()

        # messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.') 차후구현

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
        #super()메서드가 자체적으로 response생성, 페이징 처리해주기 때문에 사용
        #super()로 부모클래스의 메서드를 쓸 수 있음. redirectview를 상속받아 사용


@method_decorator(login_required, 'get')
class LikeListView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('list_themeRev')

    def get(self, *args, **kwargs):
        username = self.request.session.get('user')
        user = get_object_or_404(User, userID = username)
        article = get_object_or_404(ThemeRev, pk=kwargs['pk'])

        if Like.objects.filter(user=user, article=article).exists():
          Like.objects.filter(user=user, article=article).delete()
          article.themeRevRecom -= 1
          article.save()
          return HttpResponseRedirect(reverse('list_themeRev'))
        else:
          Like(user=user, article=article).save()

        article.themeRevRecom += 1
        article.save()

        return super(LikeListView, self).get(self.request, *args, **kwargs)


@method_decorator(login_required, 'get')
class HateArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('detail_themeRev', kwargs={'themeRev_pk':kwargs['pk']})


    def get(self, *args, **kwargs):
        username = self.request.session.get('user')
        user = get_object_or_404(User, userID = username)
        article = get_object_or_404(ThemeRev, pk=kwargs['pk'])

        if Hate.objects.filter(user=user, article=article).exists():
          Hate.objects.filter(user=user, article=article).delete()
          article.themeRevRecom -= 1
          article.save()
          return HttpResponseRedirect(reverse('detail_themeRev', kwargs={'themeRev_pk':kwargs['pk']}))
        else:
          Hate(user=user, article=article).save()

        article.themeRevRecom += 1
        article.save()
        return super(HateArticleView, self).get(self.request, *args, **kwargs)


@method_decorator(login_required, 'get')
class HateListView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('list_themeRev')

    def get(self, *args, **kwargs):
        username = self.request.session.get('user')
        user = get_object_or_404(User, userID = username)
        article = get_object_or_404(ThemeRev, pk=kwargs['pk'])

        if Hate.objects.filter(user=user, article=article).exists():
          Hate.objects.filter(user=user, article=article).delete()
          article.themeRevRecom += 1
          article.save()
          return HttpResponseRedirect(reverse('list_themeRev'))
        else:
          Hate(user=user, article=article).save()

        article.themeRevRecom -= 1
        article.save()
        return super(HateListView, self).get(self.request, *args, **kwargs)


def mypage(request):
    username = request.session.get('user')
    if User.objects.filter(userID = username).exists():
        return render(request, 'registration/mypage.html')
    return redirect('login')
