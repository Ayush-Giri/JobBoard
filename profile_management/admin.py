from django.contrib import admin
from profile_management.models import ApplicantProfile, EmployerProfile

# Register your models here.

admin.site.register(ApplicantProfile)
admin.site.register(EmployerProfile)