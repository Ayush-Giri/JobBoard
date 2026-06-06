from rest_framework import serializers
from locations.models import Country, City

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField()
    class Meta:
        model = City
        fields = [
            'id',
            'name', 
            'country',
            'country_name'
        ]

    def get_country_name(self, obj):
        return obj.country.name

