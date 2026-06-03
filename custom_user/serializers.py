from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    # password is write only field should not be sent as response
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password',
            'role',
        ]

    
    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("phone number is already in use")
        return value

    
    def to_internal_value(self, data):
        data = data.copy()
        data['phone_number'] = "+977" + data.get('phone_number')
        data['first_name'] = data.get('first_name').title()
        data['last_name'] = data.get('last_name').title()
        return super().to_internal_value(data)
    
    def create(self, validated_data):
        """
        By default the password is set as plain text in django admin panel
        for the password to be hased we have to use the create_user method
        """
        instance = User.objects.create_user(**validated_data)
        return instance
    
