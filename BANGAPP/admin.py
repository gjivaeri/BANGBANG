from django.contrib import admin
from .models import User
from .models import Shop
from .models import Shoprev
from .models import Theme
from .models import ThemeRev, Test
from .forms import TestForm, ThemeRevForm

# Register your models here.
admin.site.register(Shop)
admin.site.register(Shoprev)
admin.site.register(Theme)
# admin.site.register(ThemeRev)

@admin.register(ThemeRev)
class ThemeRevAdmin(admin.ModelAdmin):
    form = ThemeRevForm

@admin.register(Test)
class ThemeRevAdmin(admin.ModelAdmin):
    form = TestForm

class BanguserAdmin(admin.ModelAdmin):
    list_display = ('userID', 'userName')

admin.site.register(User, BanguserAdmin)
