from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, Patient, Visit, MedicalRecord
from django.db.models import Q

# =====================
# PATIENTS (DISPLAY ONLY)
# =====================
class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "app/patient_list.html"
    context_object_name = "patients"

    def get_queryset(self):
        queryset = Patient.objects.order_by("patient_id")
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) |
                Q(middle_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(contact_no__icontains=query)
            )

        return queryset



class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "app/patient_detail.html"


# =====================
# VISITS (DISPLAY ONLY)
# =====================
class VisitListView(LoginRequiredMixin, ListView):
    model = Visit
    template_name = "app/visit_list.html"
    context_object_name = "visits"

    def get_queryset(self):
        queryset = Visit.objects.order_by("visit_id")
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(patient__first_name__icontains=query) |
                Q(patient__middle_name__icontains=query) |
                Q(patient__last_name__icontains=query) |
                Q(visit_type__icontains=query) |
                Q(visit_date__icontains=query)
            )

        return queryset



class VisitDetailView(LoginRequiredMixin, DetailView):
    model = Visit
    template_name = "app/visit_detail.html"


# =====================
# MEDICAL RECORD (DISPLAY ONLY)
# =====================
class MedicalRecordListView(LoginRequiredMixin, ListView):
    model = MedicalRecord
    template_name = "app/record_list.html"
    context_object_name = "records"

    def get_queryset(self):
        queryset = MedicalRecord.objects.order_by("record_id")
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(diagnosis__icontains=query) |
                Q(treatment__icontains=query) |
                Q(visit__patient__first_name__icontains=query) |
                Q(visit__patient__middle_name__icontains=query) |
                Q(visit__patient__last_name__icontains=query)
            )

        return queryset



class MedicalRecordDetailView(LoginRequiredMixin, DetailView):
    model = MedicalRecord
    template_name = "app/record_detail.html"


# =====================
# USERS (DISPLAY ONLY)
# =====================
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "app/user_list.html"
    context_object_name = "users"


# =====================
# AUTH
# =====================
class UserLoginView(View):
    template_name = "app/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("patient-list")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, self.template_name)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logged out successfully.")
        return redirect("login")


class DashboardView(LoginRequiredMixin, View):
    template_name = "app/dashboard.html"

    def get(self, request):
        total_patients = Patient.objects.count()
        total_visits = Visit.objects.count()
        total_records = MedicalRecord.objects.count()

        context = {
            "total_patients": total_patients,
            "total_visits": total_visits,
            "total_records": total_records,
        }
        return render(request, self.template_name, context)
