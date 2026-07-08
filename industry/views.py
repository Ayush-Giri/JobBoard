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
    pagination_class = [IndustryCursorPagination]

    def list(self, request, *args, **kwargs):
        cache_key = "industries"
        cached_data = cache.get(cache_key)
        if cached_data is None:
            response_object = super().list(request, *args, **kwargs)
            cache.set(key=cache_key, value=response_object.data, timeout=CACHE_TIME_TO_LIVE)
            return response_object
        else:
            return Response(cached_data, status=status.HTTP_200_OK)
        
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        cache_key = f"industries_{pk}"
        cached_data = cache.get(cache_key)
        if cached_data is None:
            response_object = super().retrieve(request, *args, **kwargs)
            cache.set(key=cache_key, value=response_object.data, timeout=CACHE_TIME_TO_LIVE)
            return response_object
        else:
            return Response(cached_data, status=status.HTTP_200_OK)
        
    def perform_create(self, serializer):
        serializer.save()
        cache.delete(key="industries")

    
    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete(key="industries")
        cache.delete(key=f"industries_{instance.pk}")

    def perform_destroy(self, instance):
        pk = instance.pk
        instance.delete()
        cache.delete("industries")
        cache.delete(f"industries_{pk}")