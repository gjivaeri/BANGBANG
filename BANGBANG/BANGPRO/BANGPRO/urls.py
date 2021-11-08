"""BANGPRO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BANGAPP import views
from BANGAPP.views import LoginView
# LikeListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/join/', views.join, name="join"),
    path('registration/login/', LoginView.as_view(), name="login"),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name="logout"),
    path('shop/<int:shop_pk>', views.shop, name="shop"),
    path('detail/theme/<int:theme_pk>', views.detail_theme, name="detail_theme"),
    path('new/themeRev', views.new_themeRev, name="new_themeRev"),
    path('edit/themeRev/<int:themeRev_pk>', views.edit_themeRev, name="edit_themeRev"),
    path('delete/themeRev/<int:themeRev_pk>', views.delete_themeRev, name="delete_themeRev"),
    path('detail/themeRev/<int:themeRev_pk>', views.detail_themeRev, name="detail_themeRev"),
    path('list_themeRev/', views.list_themeRev, name="list_themeRev"),
    path('like/', views.like, name="like"),
    path('hate/', views.hate, name="hate"),
    path('mypage/', views.mypage, name="mypage"),
    #후에 삭제될 불필요한 코드
    # path('new/shopRev', views.new_shopRev, name="new_shopRev"),
    # path('edit/shopRev/<int:shopRev_pk>', views.edit_shopRev, name="edit_shopRev"),
    # path('delete/shopRev/<int:shopRev_pk>', views.delete_shopRev, name="delete_shopRev"),
    # path('detail/shopRev/<int:shopRev_pk>', views.detail_shopRev, name="detail_shopRev"),
]
