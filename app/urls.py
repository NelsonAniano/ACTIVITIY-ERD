from django.urls import path
from django.views.generic import RedirectView
from .views import (
    UserListView,
    PatientListView,
    PatientDetailView,
    VisitListView,
    VisitDetailView,
    MedicalRecordListView,
    MedicalRecordDetailView,
    UserLoginView,
    UserLogoutView,
    DashboardView,
)

urlpatterns = [
    # Root redirect to patient list
    path("", RedirectView.as_view(pattern_name="patient-list", permanent=False)),

    # Users
    path("users/", UserListView.as_view(), name="user-list"),

    # Patients
    path("patients/", PatientListView.as_view(), name="patient-list"),
    path("patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),

    # Visits
    path("visits/", VisitListView.as_view(), name="visit-list"),
    path("visits/<int:pk>/", VisitDetailView.as_view(), name="visit-detail"),

    # Medical Records
    path("records/", MedicalRecordListView.as_view(), name="record-list"),
    path("records/<int:pk>/", MedicalRecordDetailView.as_view(), name="record-detail"),


    # Auth
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),

    path('dashboard/', DashboardView.as_view(), name='home_dashboard'),

]
