from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from credential_verification.serializers import EmailVerificationLinkSerializer
from credential_verification.models import EmailVerificationLink

# Create your views here.

class SendVerificationLinkView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmailVerificationLinkSerializer


class VerifyEmail(RetrieveAPIView):
    # by default the request in browser is get request
    # now test this logic before implementing
    queryset = EmailVerificationLink.objects.all()
    serializer_class = EmailVerificationLinkSerializer
    lookup_field = "unique_link"
    lookup_url_kwarg = "unique_path"

    def get_object(self):
        object_instance = super().get_object()
        object_instance.is_used = True
        object_instance.save()
        return object_instance





