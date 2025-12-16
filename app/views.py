from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

from .models import (
    User,
    Patient,
    Visit,
    MedicalRecord,
    LabResult,
    Medication,
    AuditLog
)

# =====================
# HOME & ABOUT
# =====================

class HomePageView(TemplateView):
    template_name = "app/home.html"


class AboutPageView(TemplateView):
    template_name = "app/about.html"


# =====================
# USER VIEWS
# =====================

class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    model = User
    fields = "__all__"
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user-list")


class UserUpdateView(UpdateView):
    model = User
    fields = "__all__"
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user-list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("user-list")


# =====================
# PATIENT VIEWS
# =====================

class PatientListView(ListView):
    model = Patient
    template_name = "app/patient_list.html"
    context_object_name = "patients"


class PatientDetailView(DetailView):
    model = Patient
    template_name = "app/patient_detail.html"


class PatientCreateView(CreateView):
    model = Patient
    fields = "__all__"
    template_name = "app/patient_form.html"
    success_url = reverse_lazy("patient-list")


class PatientUpdateView(UpdateView):
    model = Patient
    fields = "__all__"
    template_name = "app/patient_form.html"
    success_url = reverse_lazy("patient-list")


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "app/confirm_delete.html"
    success_url = reverse_lazy("patient-list")



# =====================
# VISIT VIEWS
# =====================

class VisitListView(ListView):
    model = Visit
    template_name = "app/visit_list.html"
    context_object_name = "visits"


class VisitDetailView(DetailView):
    model = Visit
    template_name = "app/visit_detail.html"


class VisitCreateView(CreateView):
    model = Visit
    fields = "__all__"
    template_name = "app/visit_form.html"
    success_url = reverse_lazy("visit-list")


# =====================
# MEDICAL RECORD
# =====================

class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = "records/record_detail.html"


class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    fields = "__all__"
    template_name = "records/record_form.html"
    success_url = reverse_lazy("visit-list")


# =====================
# LAB RESULT
# =====================

class LabResultCreateView(CreateView):
    model = LabResult
    fields = "__all__"
    template_name = "labs/lab_form.html"
    success_url = reverse_lazy("visit-list")


# =====================
# MEDICATION
# =====================

class MedicationCreateView(CreateView):
    model = Medication
    fields = "__all__"
    template_name = "medications/medication_form.html"
    success_url = reverse_lazy("visit-list")
