from django.urls import path
from credential_verification.views import SendVerificationLinkView, VerifyEmail

urlpatterns = [
    path('email/', SendVerificationLinkView.as_view()),
    path('email/<str:unique_path>/', VerifyEmail.as_view())
]