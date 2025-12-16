from django.contrib import admin
from .models import (
    User,
    Patient,
    Visit,
    MedicalRecord,
    LabResult,
    Medication,
    AuditLog
)

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(MedicalRecord)
admin.site.register(LabResult)
admin.site.register(Medication)
admin.site.register(AuditLog)

"""
from django.contrib import admin
from .models import Post

admin.site.register(Post)
"""

