from django.contrib import admin
from .models import Doctor, Patient, Appointment



@admin.register(Doctor)
class CustomDoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "phone", "email", "image")
    search_fields = ("name", "specialty")
    fieldsets = (
        ("Main information", {"fields": ("name", "specialty", "image")}),
        ("Contacts", {"fields": ("phone", "email"), "classes": ("collapse",)}),
    )


@admin.register(Patient)
class CustomPatientAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "birth_date", "phone", "email")
    fieldsets = (
        ("Main information", {"fields": ("name", "birth_date")}),
        ("Contacts", {"fields": ("phone", "email"), "classes": ("collapse",)}),
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "doctor", "patient", "status")
    search_fields = ("doctor__name", "patient__name")

    def get_fieldsets(self, request, obj=None):
        if obj:
            return (
                ("Doctor and patient", {"fields": ("doctor", "patient")}),
                ("Date and time of appointment", {"fields": ("date", "time")}),
                (
                    "Additional info",
                    {"fields": ("reason", "status"), "classes": ("collapse",)},
                ),
            )
        else:
            return ((None, {"fields": ("doctor", "patient", "date", "time")}),)
