from rest_framework import serializers
from profile_management.models import ApplicantProfile, EmployerProfile
from locations.serializers import CountrySerializer, CitySerializer


class ApplicationProfileSerializer(serializers.ModelSerializer):
    # front end will send ids to skill to add skills 
    # and now with this skill names front end will get skill details as well
    skill_names = serializers.StringRelatedField(source='skills', many=True, read_only=True)
    city_detail = CitySerializer(source="city", read_only=True)
    country_detail = CountrySerializer(source="country", read_only=True)
    class Meta:
        model = ApplicantProfile
        fields = [
            'id',
            'date_of_birth',
            'profile_photo',
            'headline',
            'bio',
            'years_of_experience',
            'current_job_title',
            'current_company',
            'expected_salary',
            'country',
            'country_detail',
            'city',
            'city_detail',
            'skills',
            'skill_names',
            'linkedin_url',
            'github_url',
            'portfolio_url',
            'resume'
        ]


class EmployerProfileSerializer(serializers.ModelSerializer):
    city_detail = CitySerializer(source="city", read_only=True)
    country_detail = CountrySerializer(source="country", read_only=True)
    class Meta:
        model = EmployerProfile
        fields = [
            'id',
            'user',
            'company_field',
            'company_logo',
            'company description',
            'industry',
            'company_size',
            'website_url',
            'city',
            'city_detail',
            'country',
            'country_detail',
            'linked_in_company_url',
        ]
