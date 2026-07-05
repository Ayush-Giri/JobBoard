from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from credential_verification.serializers import EmailVerificationLinkSerializer
from credential_verification.models import EmailVerificationLink
from rest_framework.permissions import AllowAny

# Create your views here.

class SendVerificationLinkView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmailVerificationLinkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class VerifyEmail(RetrieveAPIView):
    # by default the request in browser is get request
    # now test this logic before implementing
    queryset = EmailVerificationLink.objects.all()
    serializer_class = EmailVerificationLinkSerializer
    lookup_field = "unique_link"
    lookup_url_kwarg = "unique_path"
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_object(self):
        object_instance = super().get_object()
        object_instance.is_used = True
        object_instance.save()
        return object_instance





