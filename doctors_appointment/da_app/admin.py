# da_app/admin.py

from django.contrib import admin
from .models import Doctor, Patient, Appointment
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(Doctor)
class CustomDoctorAdmin(admin.ModelAdmin):
    # Поля для отображения в списке
    list_display = ["get_full_name", "specialty", "phone", "get_email"]
    # Поля для поиска
    search_fields = ["user__first_name", "user__last_name", "user__email", "specialty"]

    @admin.display(description="Полное имя")
    def get_full_name(self, obj):
        # obj - это экземпляр модели Doctor
        return obj.user.get_full_name() or obj.user.email

    @admin.display(description="Email")
    def get_email(self, obj):
        return obj.user.email


@admin.register(Patient)
class CustomPatientAdmin(admin.ModelAdmin):
    list_display = ["get_full_name", "birth_date", "phone", "get_email"]
    search_fields = ["user__first_name", "user__last_name", "user__email"]

    @admin.display(description="Полное имя")
    def get_full_name(self, obj):
        # obj - это экземпляр модели Patient
        return obj.user.get_full_name() or obj.user.email

    @admin.display(description="Email")
    def get_email(self, obj):
        return obj.user.email


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "date", "time", "status")
    list_filter = ("status", "doctor", "date")
    search_fields = ("patient__user__first_name", "doctor__user__first_name", "date")
