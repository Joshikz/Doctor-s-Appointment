from django.contrib import admin
from .models import Doctor, Patient, Appointment, DoctorAttachment


admin.site.register(DoctorAttachment)
# admin.site.register(Patient)
# admin.site.register(Appointment)


@admin.register(Doctor)
class CustomDoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "phone", "email")
    search_fields = ("name", "specialty")
    fieldsets = (
        ("Основная информация", {"fields": ("name", "specialty")}),
        ("Контактные данные", {"fields": ("phone", "email"), "classes": ("collapse",)}),
    )


@admin.register(Patient)
class CustomPatientAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "birth_date", "phone", "email")
    fieldsets = (
        ("Основная информация", {"fields": ("name", "birth_date")}),
        ("Контактные данные", {"fields": ("phone", "email"), "classes": ("collapse",)}),
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "doctor", "patient", "status")
    search_fields = ("doctor__name", "patient__name")

    def get_fieldsets(self, request, obj=None):
        if obj:
            return (
                ("Доктор и пациент", {"fields": ("doctor", "patient")}),
                ("Дата и время приёма", {"fields": ("date", "time")}),
                (
                    "Дополнительно",
                    {"fields": ("reason", "status"), "classes": ("collapse",)},
                ),
            )
        else:
            return ((None, {"fields": ("doctor", "patient", "date", "time")}),)
