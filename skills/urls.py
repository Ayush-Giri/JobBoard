from django.urls import path
from skills.views import SkillView

urlpatterns = [
    path("skills/", SkillView.as_view()),
    path("skills/<int:id>/", SkillView.as_view()),
]