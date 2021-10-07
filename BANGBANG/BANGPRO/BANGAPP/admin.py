from django.contrib import admin
from .models import User
from .models import Shop
from .models import Shoprev
from .models import Theme
from .models import ThemeRev

# Register your models here.

admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Shoprev)
admin.site.register(Theme)
admin.site.register(ThemeRev)