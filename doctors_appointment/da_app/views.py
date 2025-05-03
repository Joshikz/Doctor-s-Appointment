from django.shortcuts import render
from .models import Doctor, Patient, Appointment, DoctorAttachment

# Create your views here.


# Show all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    for doctor in doctors:
        att = DoctorAttachment.objects.filter(doctor_id=doctor.pk)
        doctor.image = att[0]
    return render(request, "da_app/doctor_list.html", {"doctors": doctors})


def doctor_detail(request, d_id):
    doctor = Doctor.objects.get(pk=d_id)
    images = DoctorAttachment.objects.filter(doctor_id=d_id)
    return render(
        request, "da_app/doctor_detail.html", {"doctor": doctor, "images": images}
    )


# Show all patients
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "da_app/patient_list.html", {"patients": patients})


def patient_detail(request, p_id):
    patients = Patient.objects.get(pk=p_id)
    return render(request, "da_app/patient_detail.html", {"patient": patients})


# Show all appointments
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(
        request, "da_app/appointment_list.html", {"appointment": appointments}
    )
