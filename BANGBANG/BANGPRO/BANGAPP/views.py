from django.contrib import auth
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import User, Shop, Shoprev, Theme, ThemeRev, Like, Hate
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#for loginview
from .forms import LoginForm, ThemeRevForm
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

# Create your views here.

def home2(request):
  theme = Theme.objects.all()
  theme1 = {'theme1': theme}
  return render(request, 'home2.html', theme1)

def home2_detail(request, theme_pk):
  theme = Theme.objects.get(pk=theme_pk)
  review = ThemeRev.objects.filter(theme_ID=theme_pk)
  return render(request, 'home2_detail.html', {'theme': theme, 'review':review})

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

#검색기능, Q객체사용불가
# class SearchFormView(FormView):
#     form_class = PostSearchForm
#     template_name = 'home.html'

#     def form_valid(self, form):
#         searchWord = form.cleaned_data['search_word']
#         post_list = Theme.objects.filter(Q(themeName=searchWord) | Q(themeGenre=searchWord) | Q(themeIntro=searchWord)).distinct()

#         context = {}
#         context['form'] = form
#         context['search_term'] = searchWord
#         context['object_list'] = post_list

#         return render(self.request, self.template_name, context)


def home(request):
    username = request.session.get('user')
    user = User.objects.filter(userID = username).values('userID')
    themes = Theme.objects.all()
    shops = Shop.objects.all()
    themescount = themes.count()
    shopscount = shops.count()
    content = {'user' : user, 'themes' : themes, 'shops' : shops, 'themescount' : themescount, 'shopscount' : shopscount}
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
    
#개발중 임시 view
def detail_themeRevAdd(request, theme_pk):
  info = Theme.objects.filter(theme_ID=theme_pk)
  theme = Theme.objects.get(pk=theme_pk)
  reviews = ThemeRev.objects.filter(theme_ID=theme_pk)
  return render(request, 'detail_themeRevAdd.html', {'theme':theme ,'reviews': reviews, 'info': info})

def detail_themeRevAddDetail(request):
  return render(request, 'detail_themeRevAddDetail.html')
#theme Review
# @login_required(login_url="/registration/login")
# def new_themeRev(request):
#     username = request.session.get('user')
#     if User.objects.filter(userID = username).exists():
#       if request.method == "POST":
#           new_themeRev = ThemeRev.objects.create(
#             themeRevTitle=request.POST["themeRevTitle"],
#             themeRevRating=request.POST["themeRevRating"],
#             themeRevDifficulty=request.POST["themeRevDifficulty"],
#             themeRevHorror=request.POST["themeRevHorror"],
#             themeRevActivity=request.POST["themeRevActivity"],
#             themeRevContent=request.POST["themeRevContent"],
#             themeRevImage=request.POST["themeRevImage"],
#             themeRevResult=request.POST["themeRevResult"],
#             themeRevOccurredTime=request.POST["themeRevOccurredTime"],
#             themeRevDate=request.POST["themeRevDate"],
#             #themeRev_WriterID=request.user,
#           )
#           return redirect("detail_themeRev", new_themeRev.pk)
#       return render(request, "new_themeRev.html")
#     else:
#       return render(request, 'registration/join.html')
def new_themeRev(request):
  form = ThemeRevForm()

  if request.method == "POST":
    print(request.POST)
    form = ThemeRevForm(request.POST)
    if form.is_valid():
      form.save()
      
  context = {'form':form}
  return render(request, "new_themeRev.html", context)

def rateTheme(request):
  if request.method == 'POST':
    el_id = request.POST.get('el_id')
    val = request.POST.get('val')
    obj = Theme.objects.get(id=el_id)
    obj.themeRating = val
    obj.save
    return JsonResponse({'success':'true', 'score': val}, safe=False)
  return JsonResponse({'success':'false'})

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
    reviews = ThemeRev.objects.all()
    themeRev = ThemeRev.objects.get(pk=themeRev_pk)
    if request.method == "POST":
        return redirect('detail_themeRev', themeRev_pk)

    return render(request, 'detail_themeRev.html', {'reviews':reviews, 'themeRev': themeRev})


def delete_themeRev(request, themeRev_pk):
    themeRev = ThemeRev.objects.get(pk=themeRev_pk)
    themeRev.delete()
    return redirect('detail_themeRev')


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
    #차후 구현할 페이지 파트
    paginator = Paginator(sorted,9)
    page = request.GET.get('page','')
    posts = paginator.get_page(page)
    #url에서 page=? 에 들어가는 값. 몇페이지의 정보를 보내는지 알아냄. 공백이어도 허용
    #분할될 객체 / 한페이지에 담길 객체 수
    #페이지 번호를 받아 해당 페이지를 리턴
    
    content = {
      'posts':posts, 'themes':themes, 'sort':sorted, 'reviews':reviews, 'shops':shops
    }
    return render(request,'list_themeRev.html', content)


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
    content = {'user' : user, 'themes' : themes}
    return render(request, 'recommend.html', content)
    



#SHOP Review 검토 후 삭제
# # @login_required(login_url="/registration/login")
# def new_shopRev(request):
#     username = request.session.get('user')
#     if User.objects.filter(userID = username).exists():
#       if request.method == "POST":
#           new_shopRev = Shoprev.objects.create(
#             shopRevTitle=request.POST["shoprevTitle"],
#             shopRevRating=request.POST["shopRating"],
#             shopRevContent=request.POST["shoprevCont"],
#             shopRevImage=request.POST["shoprevImage"],
#             shopRevDate=request.POST["shoprevDate"],
#             shopRevWriteDate=request.POST["shoprevWDate"],
#             shopRev_WriterID=request.user,
#           )
#           return redirect("detail_shopRev", new_shopRev.pk)
#       return render(request, "new_shopRev.html")
#     else:
#       return render(request, 'registration/join.html')
    

# def edit_shopRev(request, shopRev_pk):
#     shopRev = Shoprev.objects.get(pk=shopRev_pk)

#     if request.method == "POST":
#         shopRev.objects.filter(pk=shopRev_pk).update(
#            shopRevTitle=request.POST["shopRevTitle"],
#            shopRevRating=request.POST["shopRevRating"],
#            shopRevContent=request.POST["shopRevContent"],
#            shopRevImage=request.POST["shopRevImage"],
#            shopRevDate=request.POST["shopRevDate"],
#            shopRevWriteDate=request.POST["shopRevWriteDate"],
#            shopRev_WriterID=request.user,
#         )
#         return redirect('detail_shopRev', shopRev_pk)

#     return render(request, 'edit_shopRev.html', {'shopRev': shopRev})

# def delete_shopRev(request, shopRev_pk):
#     shopRev = Shoprev.objects.get(pk=shopRev_pk)
#     shopRev.delete()
#     return redirect('/shop/<int:shopRev_pk>')

