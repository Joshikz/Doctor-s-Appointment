from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")  # имя врача
    specialty = models.CharField(
        max_length=100, verbose_name="Специальность"
    )  # специальность
    phone = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Телефон"
    )  # телефон врача
    email = models.EmailField(
        null=True, blank=True, verbose_name="Эл. почта"
    )  # электронная почта

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self):
        return f"{self.name} ({self.specialty})"


class Patient(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")  # имя пациента
    birth_date = models.DateField(verbose_name="Дата рождения")  # дата рождения
    phone = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Телефон"
    )  # телефон пациента
    email = models.EmailField(
        null=True, blank=True, verbose_name="Эл. почта"
    )  # электронная почта

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, verbose_name="Доктор"
    )  # связь с доктором
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name="Пациент"
    )  # связь с пациентом
    date = models.DateField(verbose_name="Дата приема")  # дата приёма
    time = models.TimeField(verbose_name="Время приема")  # время приёма
    reason = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Причина визита"
    )  # причина визита
    status = models.CharField(
        max_length=20,
        choices=[
            ("Scheduled", "Запланирован"),
            ("Completed", "Завершен"),
            ("Cancelled", "Отменен"),
        ],
        default="Scheduled",
        verbose_name="Статус записи",
    )  # статус записи

    class Meta:
        verbose_name = "Приём"
        verbose_name_plural = "Приёмы"

    def __str__(self):
        return f"{self.date} {self.time} — {self.patient.name} у {self.doctor.name}"


class DoctorAttachment(models.Model):
    verbose_name = "Фото Доктора"
    image = models.ImageField(upload_to="image", verbose_name="Фото профиля")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Доктор")

    def save(self, *args, **kwargs):
        self.name = self.image.name.split(".")[0].capitalize()
        super().save(*args, **kwargs)
