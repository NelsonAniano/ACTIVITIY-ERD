from django.contrib import admin
from .models import Patient, Visit, MedicalRecord, LabResult, Medication, AuditLog, User


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "middle_name", "last_name", "age", "gender")
    search_fields = ("first_name", "last_name")


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("visit_id", "patient", "visit_date", "visit_type")


admin.site.register(User)
admin.site.register(MedicalRecord)
admin.site.register(LabResult)
admin.site.register(Medication)
admin.site.register(AuditLog)


"""
from django.contrib import admin
from .models import Post

admin.site.register(Post)
"""

