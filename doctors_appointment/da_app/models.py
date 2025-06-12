from django.db import models

# from user.models import User # Если User находится в отдельном приложении 'user', то это правильно.
from django.conf import settings
from django.utils.translation import gettext_lazy as _  # Импортируем gettext_lazy


class Doctor(models.Model):
    # OneToOneField гарантирует, что у одного пользователя может быть только один профиль врача
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    specialty = models.CharField(
        max_length=100, verbose_name=_("Specialty")
    )  # Добавлено verbose_name
    phone = models.CharField(
        max_length=15, null=True, blank=True, verbose_name=_("Phone")
    )  # Добавлено verbose_name
    image = models.ImageField(
        upload_to="image/",
        null=True,
        blank=True,
        verbose_name=_("Doctor's image"),  # Уже было, но обернул в _()
    )

    def __str__(self):
        # Берем имя и фамилию из связанной модели User
        return f"{self.user.first_name} {self.user.last_name} ({self.specialty})"


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    birth_date = models.DateField(
        null=True, blank=True, verbose_name=_("Birth date")
    )  # Добавлено verbose_name
    phone = models.CharField(
        max_length=15, null=True, blank=True, verbose_name=_("Phone")
    )  # Добавлено verbose_name

    def __str__(self):
        return self.user.get_full_name() or self.user.email


class Appointment(models.Model):
    # Теперь мы ссылаемся на профили, которые связаны с пользователями
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name=_("Patient")
    )  # Добавлено verbose_name
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, verbose_name=_("Doctor")
    )  # Добавлено verbose_name
    date = models.DateField(verbose_name=_("Date"))  # Добавлено verbose_name
    time = models.TimeField(verbose_name=_("Time"))  # Добавлено verbose_name
    reason = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Reason")
    )  # Добавлено verbose_name
    status = models.CharField(
        max_length=20,
        choices=[
            ("Scheduled", _("Scheduled")),  # Обернуто в _()
            ("Completed", _("Completed")),  # Обернуто в _()
            ("Cancelled", _("Cancelled")),  # Обернуто в _()
        ],
        default="Scheduled",
        verbose_name=_("Status"),  # Добавлено verbose_name
    )

    def __str__(self):
        # Обратите внимание, как мы получаем имена через связанные модели
        return f"{self.date} {self.time} — {self.patient.user.first_name} with Dr. {self.doctor.user.first_name}"
