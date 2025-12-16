"""
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
        """

from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    contact_no = models.CharField(max_length=20)
    emergency_contact = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_date = models.DateField()
    visit_type = models.CharField(max_length=50)
    reason = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Visit {self.visit_id} - {self.patient}"


class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    visit = models.OneToOneField(Visit, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescriptions_summary = models.TextField()
    next_followup_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Medical Record {self.record_id}"


class LabResult(models.Model):
    lab_id = models.AutoField(primary_key=True)
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    units = models.CharField(max_length=50)
    date_performed = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.test_name


class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AuditLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.action}"


