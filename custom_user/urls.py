from django.urls import path
from custom_user.views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view()),
]