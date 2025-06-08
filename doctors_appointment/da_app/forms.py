from django import forms
from .models import Doctor, Patient, Appointment


# Новая форма для создания профиля Врача
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # Указываем поля, которые есть в модели Doctor
        # Поле 'user' позволит выбрать пользователя из списка
        fields = ["user", "specialty", "phone", "image"]


# Новая форма для создания профиля Пациента
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        # Указываем поля, которые есть в модели Patient
        fields = ["user", "birth_date", "phone"]


# Новая форма для создания Записи на прием
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        # Поле 'patient' убрано, т.к. оно будет заполняться автоматически в представлении
        fields = ["doctor", "date", "time", "reason", "status"]
