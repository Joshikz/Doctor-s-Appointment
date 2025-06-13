from django.urls import path
from .views import (
    doctor_list,
    doctor_detail,
    doctor_create,
    doctor_update,
    doctor_delete,
    patient_list,
    patient_create,
    patient_detail,
    patient_update,
    patient_delete,
    appointment_list,
    appointment_create,
    appointment_update,
    appointment_delete,
    appointment_detail,
)

urlpatterns = [
    path("", doctor_list, name="doctor_list"),
    path("doctors/<int:d_id>/", doctor_detail, name="doc-details-page"),
    path('doctors/create/', doctor_create, name='doctor_create'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/update/<int:d_id>/', doctor_update, name='doctor_update'),
    path('doctors/delete/<int:d_id>/', doctor_delete, name='doctor_delete'),
    path('patients/create/', patient_create, name='patient_create'),
    path("patients/", patient_list, name="patient_list"),
    path("patients/<int:p_id>/", patient_detail, name="pat-details-page"),
    path('patients/update/<int:p_id>/', patient_update, name='patient_update'),
    path('patients/delete/<int:p_id>/', patient_delete, name='patient_delete'),
    path("appointments/", appointment_list, name="appointment_list"),
    path("appointments/create/", appointment_create, name="appointment_create"),
    path("appointments/<int:a_id>/", appointment_detail, name="appointment_detail"),
    path('appointments/update/<int:a_id>/', appointment_update, name='appointment_update'),
    path('appointments/delete/<int:a_id>/', appointment_delete, name='appointment_delete'),
    
]
