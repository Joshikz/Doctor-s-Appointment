from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment
from .forms import DoctorForm, PatientForm, AppointmentForm
# Create your views here.


# Show all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "da_app/doctor_list.html", {"doctors": doctors})


def doctor_detail(request, d_id):
    doctor = Doctor.objects.get(pk=d_id)
    return render(
        request, 
        "da_app/doctor_detail.html", 
        {"doctor": doctor}
    )

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save() 
            return redirect('doctor_list') 
    else:
        form = DoctorForm()
    return render(request, 'da_app/doctor_create.html', {'form': form})

def doctor_update(request, d_id):
    doctor = Doctor.objects.get(pk=d_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)  
        if form.is_valid():
            form.save() 
            return redirect('doctor_list') 
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'da_app/doctor_create.html', {'form': form})

def doctor_delete(request, d_id):
    doctor = Doctor.objects.get(pk=d_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'da_app/doctor_delete.html', {'doctor': doctor})

# Show all patients
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "da_app/patient_list.html", {"patients": patients})



def patient_detail(request, p_id):
    patients = Patient.objects.get(pk=p_id)
    return render(request, "da_app/patient_detail.html", {"patient": patients})


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save() 
            return redirect('patient_list') 
    else:
        form = PatientForm()
    return render(request, 'da_app/patient_create.html', {'form': form})

def patient_update(request, p_id):
    patient = Patient.objects.get(pk=p_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)  
        if form.is_valid():
            form.save() 
            return redirect('patient_list') 
    else:
        form = PatientForm(instance=patient)
    return render(request, 'da_app/patient_create.html', {'form': form})

def patient_delete(request, p_id):
    patient = Patient.objects.get(pk=p_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'da_app/patient_delete.html', {'patient': patient})

# Show all appointments
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(
        request, "da_app/appointment_list.html", {"appointment": appointments}
    )

def appointment_detail(request, a_id):
    appointment = Appointment.objects.get(pk=a_id)
    return render(
        request, 
        "da_app/appointment_detail.html", 
        {"appointment": appointment}
    )

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save() 
            return redirect('appointment_list') 
    else:
        form = AppointmentForm()
    return render(request, 'da_app/appointment_create.html', {'form': form})

def appointment_update(request, a_id):
    appointment = Appointment.objects.get(pk=a_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appointment)  
        if form.is_valid():
            form.save() 
            return redirect('appointment_list') 
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'da_app/appointment_create.html', {'form': form})

def appointment_delete(request, a_id):
    appointment = Appointment.objects.get(pk=a_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'da_app/appointment_delete.html', {'appointment': appointment})