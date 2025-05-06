from django import forms
from .models import Doctor, Patient, Appointment


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'phone', 'email', 'image']

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['name', 'birth_date', 'phone', 'email']

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'time', 'reason', 'status']