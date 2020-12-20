from django.contrib import admin
from .models import Promo,AdminUser,NormalUser;
# Register your models here.
admin.site.register([Promo,NormalUser,AdminUser]);
