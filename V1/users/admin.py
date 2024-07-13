from django.contrib import admin
from .models import Cuser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Cuser,UserAdmin)
# Register your models here.
