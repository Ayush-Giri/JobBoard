from rest_framework import serializers
from skills.models import Skills


class SkillSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Skills
        fields = [
            'id',
            'name',
            'user',
            'username'
        ]

    
    def get_username(self, obj):
        return obj.user.username