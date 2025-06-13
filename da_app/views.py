from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment
from .forms import DoctorForm, PatientForm, AppointmentForm
from django.contrib.auth.decorators import login_required
from .decorators import group_required
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, user_passes_test


def is_superuser(user):
    return user.is_superuser


# Create your views here.


# Show all doctors
@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "da_app/doctor_list.html", {"doctors": doctors})


@login_required
def doctor_detail(request, d_id):
    doctor = Doctor.objects.get(pk=d_id)
    return render(request, "da_app/doctor_detail.html", {"doctor": doctor})


@login_required
@user_passes_test(is_superuser)
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("doctor_list")
    else:
        form = DoctorForm()
    return render(request, "da_app/doctor_create.html", {"form": form})


@login_required
@user_passes_test(is_superuser)
def doctor_update(request, d_id):
    doctor = Doctor.objects.get(pk=d_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctor_list")
    else:
        form = DoctorForm(instance=doctor)
    return render(request, "da_app/doctor_create.html", {"form": form})


@login_required
@user_passes_test(is_superuser)
def doctor_delete(request, d_id):
    doctor = Doctor.objects.get(pk=d_id)
    if request.method == "POST":
        doctor.delete()
        return redirect("doctor_list")
    return render(request, "da_app/doctor_delete.html", {"doctor": doctor})


# Show all patients
@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "da_app/patient_list.html", {"patients": patients})


@login_required
def patient_detail(request, p_id):
    requested_patient = get_object_or_404(Patient, pk=p_id)

    current_user = request.user

    if requested_patient.user == current_user or current_user.is_superuser:
        return render(
            request, "da_app/patient_detail.html", {"patient": requested_patient}
        )
    else:

        raise PermissionDenied


def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("patient_list")
    else:
        form = PatientForm()
    return render(request, "da_app/patient_create.html", {"form": form})


def patient_update(request, p_id):
    patient = Patient.objects.get(pk=p_id)
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect("patient_list")
    else:
        form = PatientForm(instance=patient)
    return render(request, "da_app/patient_create.html", {"form": form})


def patient_delete(request, p_id):
    patient = Patient.objects.get(pk=p_id)
    if request.method == "POST":
        patient.delete()
        return redirect("patient_list")
    return render(request, "da_app/patient_delete.html", {"patient": patient})


# Show all appointments
@login_required
def appointment_list(request):
    user = request.user
    if user.groups.filter(name="Doctors").exists():
        appointments = Appointment.objects.filter(doctor__user=user)
    elif user.groups.filter(name="Patients").exists():
        appointments = Appointment.objects.filter(patient__user=user)
    elif user.is_superuser:
        appointments = Appointment.objects.all()
    else:
        appointments = []

    return render(
        request, "da_app/appointment_list.html", {"appointments": appointments}
    )


def appointment_detail(request, a_id):
    appointment = Appointment.objects.get(pk=a_id)
    return render(
        request, "da_app/appointment_detail.html", {"appointment": appointment}
    )


@login_required
@group_required(["Patients"])
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)
            appointment.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm()
    return render(request, "da_app/appointment_create.html", {"form": form})


@login_required
@group_required(["Doctors", "Patients"])
def appointment_update(request, a_id):
    appointment = Appointment.objects.get(pk=a_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, request.FILES, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, "da_app/appointment_create.html", {"form": form})


def appointment_delete(request, a_id):
    appointment = Appointment.objects.get(pk=a_id)
    if request.method == "POST":
        appointment.delete()
        return redirect("appointment_list")
    return render(
        request, "da_app/appointment_delete.html", {"appointment": appointment}
    )
