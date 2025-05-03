from django.urls import path
from .views import (
    doctor_list,
    doctor_detail,
    patient_list,
    patient_detail,
    appointment_list,
)

urlpatterns = [
    path("", doctor_list, name="doctor_list"),
    path("doctors/<int:d_id>/", doctor_detail, name="doc-details-page"),
    path("patients/", patient_list, name="patient_list"),
    path("patients/<int:p_id>/", patient_detail, name="pat-details-page"),
    path("appointments/", appointment_list, name="appointment_list"),
]
