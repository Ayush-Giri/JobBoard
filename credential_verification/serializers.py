from rest_framework.serializers import ModelSerializer
from credential_verification.models import EmailVerificationLink

class EmailVerificationLinkSerializer(ModelSerializer):
    class Meta:
        model = EmailVerificationLink
        fields = "__all__"