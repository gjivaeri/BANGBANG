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
from django.conf import settings
from django.conf.urls.static import static

# LikeListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registration/join/', views.join, name="join"),
    path('registration/login/', LoginView.as_view(), name="login"),
    path('home/', views.home, name='home'),
    path('recommend/', views.recommend, name='recommend'),
    path('logout/', views.logout, name="logout"),
    path('detail/theme/<int:theme_pk>', views.detail_theme, name="detail_theme"),
    path('new/themeRev', views.new_themeRev, name="new_themeRev"),
    path('new/themeRevTest', views.new_themeRevTest, name="new_themeRevTest"),
    path('edit/themeRev/<int:themeRev_pk>', views.edit_themeRev, name="edit_themeRev"),
    path('delete/themeRev/<int:themeRev_pk>', views.delete_themeRev, name="delete_themeRev"),
    path('detail/themeRev/<int:themeRev_pk>', views.detail_themeRev, name="detail_themeRev"),
    path('list_themeRev/', views.list_themeRev, name="list_themeRev"),
    path('list_themeRevAll/', views.list_themeRevAll, name="list_themeRevAll"),
    path('like/', views.like, name="like"),
    path('hate/', views.hate, name="hate"),
    path('selectImg/', views.selectImg, name="selectImg"),
    path('mypage/', views.mypage, name="mypage"),
    path('detail/themeRev/themeRevAdd/<int:theme_pk>', views.detail_themeRevAdd, name="detail_themeRevAdd"),
    path('detail/themeRev/themeRevAdd/<int:theme_pk>/<int:review_pk>', views.detail_themeRevAddDetail, name="detail_themeRevAddDetail"),
    path('mypage/mylike/', views.mylike, name="mylike"),
    path('mypage/myreview/', views.myreview, name="myreview"),
    path('detail/shop/<int:shop_pk>', views.detail_shop, name="detail_shop"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
