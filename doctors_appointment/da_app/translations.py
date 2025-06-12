# da_app/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import Doctor, Patient, Appointment
# Строка "from user.models import User" больше не нужна, удаляем ее

# --- Перевод для модели Doctor ---
@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('specialty',)

# --- Блок для User отсюда удален ---

# --- Ваши остальные переводы ---
@register(Appointment)
class AppointmentTranslations(TranslationOptions):
    fields = ('reason', 'status')

@register(Patient)
class PatientTranslations(TranslationOptions):
    fields = ('phone',)