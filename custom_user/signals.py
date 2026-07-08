from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from profile_management.models import ApplicantProfile, EmployerProfile

User = get_user_model()



@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == "applicant":
            ApplicantProfile.objects.create(
                user=instance 
            )
        EmployerProfile.objects.create(user=instance)



