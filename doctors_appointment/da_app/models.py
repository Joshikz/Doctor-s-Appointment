from django.db import models
from user.models import User
from django.conf import settings


class Doctor(models.Model):
    # OneToOneField гарантирует, что у одного пользователя может быть только один профиль врача
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(
        upload_to="image/",
        null=True,
        blank=True,
        verbose_name="Doctor's image",
    )

    def __str__(self):
        # Берем имя и фамилию из связанной модели User
        return f"{self.user.first_name} {self.user.last_name} ({self.specialty})"


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.email


class Appointment(models.Model):
    # Теперь мы ссылаемся на профили, которые связаны с пользователями
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Scheduled", "Scheduled"),
            ("Completed", "Completed"),
            ("Cancelled", "Cancelled"),
        ],
        default="Scheduled",
    )

    def __str__(self):
        # Обратите внимание, как мы получаем имена через связанные модели
        return f"{self.date} {self.time} — {self.patient.user.first_name} with Dr. {self.doctor.user.first_name}"
