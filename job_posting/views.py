from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from job_posting.models import JobPosting
from custom_permissions import IsEmployer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class JobPostingViewset(ModelViewSet):

    def get_queryset(self):
        if self.request.user.role == "applicant":
            return JobPosting.objects.all()
        else:
            return JobPosting.objects.filter(user=self.request.user)
    

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsEmployer]
        return [permission() for permission in permission_classes]
    
    
    @action(detail=True, methods=["patch"], name="deactivate")
    def deactivate_job(self, request, pk=None):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(
            {"is_active":False},
            status=status.HTTP_200_OK
        )








