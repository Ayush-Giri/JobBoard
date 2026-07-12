from django.urls import path
from profile_management.views import MeView


urlpatterns = [
    path('me/', MeView.as_view())
]