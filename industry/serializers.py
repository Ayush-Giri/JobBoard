from rest_framework.serializers import ModelSerializer
from industry.models import Industry


class IndustrySerializer(ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"