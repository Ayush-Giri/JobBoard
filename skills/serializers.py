from rest_framework.serializers import ModelSerializer
from skills.models import Skills


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"