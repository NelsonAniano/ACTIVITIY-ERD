from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,

    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,

    PatientListView,
    PatientDetailView,
    PatientCreateView,
    PatientUpdateView,
    PatientDeleteView,

    VisitListView,
    VisitDetailView,
    VisitCreateView,

    MedicalRecordDetailView,
    MedicalRecordCreateView,

    LabResultCreateView,
    MedicationCreateView,
)

urlpatterns = [

    # HOME
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),

    # USERS
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/add/", UserCreateView.as_view(), name="user-add"),
    path("users/<int:pk>/edit/", UserUpdateView.as_view(), name="user-edit"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),

    # PATIENTS
    path("patients/", PatientListView.as_view(), name="patient-list"),
    path("patients/add/", PatientCreateView.as_view(), name="patient-add"),
    path("patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
    path("patients/<int:pk>/edit/", PatientUpdateView.as_view(), name="patient-edit"),
    path("patients/<int:pk>/delete/", PatientDeleteView.as_view(), name="patient-delete"),

    # VISITS
    path("visits/", VisitListView.as_view(), name="visit-list"),
    path("visits/add/", VisitCreateView.as_view(), name="visit-add"),
    path("visits/<int:pk>/", VisitDetailView.as_view(), name="visit-detail"),

    # MEDICAL RECORD
    path("records/add/", MedicalRecordCreateView.as_view(), name="record-add"),
    path("records/<int:pk>/", MedicalRecordDetailView.as_view(), name="record-detail"),

    # LAB & MEDICATION
    path("labs/add/", LabResultCreateView.as_view(), name="lab-add"),
    path("medications/add/", MedicationCreateView.as_view(), name="medication-add"),
]

