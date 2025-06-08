# user/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Эта команда регистрирует вашу кастомную модель User в админ-панели
# со стандартным интерфейсом UserAdmin.
admin.site.register(User, UserAdmin)
