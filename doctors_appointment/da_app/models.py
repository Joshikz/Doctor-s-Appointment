from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)  # doctors name
    specialty = models.CharField(max_length=100)  # spetialty
    phone = models.CharField(max_length=15, null=True, blank=True)  # doctors phone
    email = models.EmailField(null=True, blank=True)  # email
    image = models.ImageField(
        upload_to="image/",
        null=True,
        blank=True,
        verbose_name="Doctor's image",
    )

    def __str__(self):
        return f"{self.name} ({self.specialty})"

class Patient(models.Model):
    name = models.CharField(max_length=100)  # patient name
    birth_date = models.DateField()  # date of birth
    phone = models.CharField(max_length=15, null=True, blank=True)  # patinet phone
    email = models.EmailField(null=True, blank=True)  # email

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # link to doctor
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # link to patient
    date = models.DateField()  # appointment date
    time = models.TimeField()  # appointment time
    reason = models.CharField(max_length=255, null=True, blank=True)  # reason for visit
    status = models.CharField(
        max_length=20,
        choices=[
            ("Scheduled", "Scheduled"),
            ("Completed", "Completed"),
            ("Cancelled", "Cancelled"),
        ],
        default="Scheduled",
    )  # appointment status

    def __str__(self):
        return f"{self.date} {self.time} — {self.patient.name} with {self.doctor.name}"



