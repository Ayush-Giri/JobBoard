from rest_framework.serializers import ModelSerializer
from industry.models import Industry


class IndustrySerializer(ModelSerializer):
    class Meta:
        fields = "__all__"