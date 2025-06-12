# user/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import User
from da_app.models import Doctor

# Сначала снимаем с регистрации стандартную админку для User
#admin.site.unregister(User)

# Создаем "встраиваемую" форму для модели Doctor
class DoctorInline(admin.StackedInline):
    model = Doctor
    can_delete = False
    verbose_name_plural = 'Doctor Profile'

# Создаем кастомную админку для User
class CustomUserAdmin(BaseUserAdmin, TabbedTranslationAdmin):
    inlines = (DoctorInline,)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    
    # Это важно, чтобы в форме редактирования отображались все нужные поля
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Регистрируем модель User с нашими новыми настройками
admin.site.register(User, CustomUserAdmin)