from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from industry.models import Industry
from rest_framework.permissions import IsAuthenticated
from industry.serializers import IndustrySerializer
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status
from pagination import IndustryCursorPagination

# Create your views here.

CACHE_TIME_TO_LIVE = 15 * 60


class IndustryViewset(ModelViewSet):
    queryset = Industry.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = IndustrySerializer
    pagination_class = IndustryCursorPagination

    