from modeltranslation.translator import register, TranslationOptions
from .models import Appointment, Doctor, Patient

@register(Appointment)
class AppointmentTranslations(TranslationOptions):
    fields = ('reason', 'status')

@register(Doctor)
class DoctorTranslations(TranslationOptions):
    fields = ('specialty',)

@register(Patient)
class PatientTranslations(TranslationOptions):
    fields = ('phone',)