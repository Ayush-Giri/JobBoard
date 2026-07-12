from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from profile_management.serializers import ApplicationProfileSerializer, EmployerProfileSerializer
from profile_management.models import ApplicantProfile, EmployerProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == "applicant":
            object = get_object_or_404(ApplicantProfile, user=request.user)
            serializer = ApplicationProfileSerializer(object)
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )
        else:
            object = get_object_or_404(EmployerProfile, user=request.user)
            serializer = EmployerProfileSerializer(object)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
    
    def patch(self, request):
        if request.user.role == "applicant":
            object = get_object_or_404(ApplicantProfile, user=request.user)
            serializer = ApplicationProfileSerializer(object, data=self.request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST
                )
            
        object = get_object_or_404(EmployerProfile, user=request.user)
        serializer = EmployerProfileSerializer(object, data=self.request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


            



    







