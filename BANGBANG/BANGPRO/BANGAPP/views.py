from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import User, Shop, Shoprev, Theme, ThemeRev, Like
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#for loginview
from .forms import LoginForm
from argon2 import PasswordHasher, exceptions
#for likeview
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import RedirectView



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
        return redirect('home')

def login(request):
    loginform = LoginForm()
    context = { 'forms' : loginform }
    if request.method == 'GET':
        return render(request, 'registration/login.html', context=context)

    elif request.method == 'POST':
        loginform = LoginForm(request.POST)
        
        if loginform.is_valid():
            return redirect('home')

        else:
           context['forms'] = loginform
           if loginform.errors:
              for value in loginform.errors.values():
                  context['error'] = value
        return render(request, 'registration/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')


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
@login_required(login_url="/registration/login")
def new_themeRev(request):
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
    return render(request, "new_themeRev.html")

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
@login_required(login_url="/registration/login")
def new_shopRev(request):
    if request.method == "POST":
        new_shopRev = Shoprev.objects.create(
           shopRevTitle=request.POST["shopRevTitle"],
           shopRevRating=request.POST["shopRevRating"],
           shopRevContent=request.POST["shopRevContent"],
           shopRevImage=request.POST["shopRevImage"],
           shopRevDate=request.POST["shopRevDate"],
           shopRevWriteDate=request.POST["shopRevWriteDate"],
           shopRev_WriterID=request.user,
        )
        return redirect("detail_shopRev", new_shopRev.pk)
    return render(request, "new_shopRev.html")

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
        return reverse('detail_themeRev', kwargs={'pk':kwargs['pk']})

    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(ThemeRev, pk=kwargs['pk'])
        #pk가 존재하는 shoprev가 있으면 가져오고 아님 404에러발생

        if Like.objects.filter(user=user, article=article).exists():
          messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 가능합니다.')
          return HttpResponseRedirect(reverse('detail_themeRev', kwargs={'pk':kwargs['pk']}))
        else:
          Like(user=user, article=article).save()

        article.like += 1
        article.save()

        messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)