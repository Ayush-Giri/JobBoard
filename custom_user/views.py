from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from custom_user.serializers import CustomUserSerializer
from throttle import UserSignupTrottle


# Create your views here.

class CreateUserView(CreateAPIView):
    serializer_class = CustomUserSerializer
    throttle_classes = [UserSignupTrottle]
    permission_classes = []
    authentication_classes = []
    





