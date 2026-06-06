from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from locations.serializers import CountrySerializer, CitySerializer
from locations.models import Country, City
from pagination import BasicPagination
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

CACHE_TIME_TO_LIVE = 15 * 60

class CountryViewset(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = BasicPagination

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    
    def list(self, request, *args, **kwargs):
        cache_key = "countries"
        cached_data = cache.get(cache_key)
        if cached_data is None:
            response_object = super().list(request, *args, **kwargs)
            cache.set(key=cache_key, value=response_object.data, timeout=CACHE_TIME_TO_LIVE)
            return response_object
        else:
            return Response(cached_data, status=status.HTTP_200_OK)
        
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        cache_key = f"countries_{pk}"
        cached_data = cache.get(cache_key)
        if cached_data is None:
            response_object = super().retrieve(request, *args, **kwargs)
            cache.set(key=cache_key, value=response_object.data, timeout=CACHE_TIME_TO_LIVE)
            return response_object
        else:
            return Response(cached_data, status=status.HTTP_200_OK)
        
    def perform_create(self, serializer):
        serializer.save()
        cache.delete(key="countries")

    
    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete(key="countries")
        cache.delete(key=f"countries_{instance.pk}")

    def perform_destroy(self, instance):
        pk = instance.pk
        instance.delete()
        cache.delete("countries")
        cache.delete(f"countries_{pk}")




class CityViewset(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = BasicPagination


    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def list(self, request, *args, **kwargs):
        cache_key = "cities"
        cached_data = cache.get(key=cache_key)
        if cached_data is None:
            reponse_object = super().list(request, *args, **kwargs)
            cache.set(key=cache_key, value=reponse_object.data, timeout=CACHE_TIME_TO_LIVE)
            return reponse_object
        else:
            return Response(cached_data, status=status.HTTP_200_OK)
        
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        cache_key = f"cities_{pk}"
        cached_data = cache.get(cache_key)
        if cached_data is None:
            response_object = super().retrieve(request, *args, **kwargs)
            cache.set(key=cache_key, value=response_object.data, timeout=CACHE_TIME_TO_LIVE)
            return response_object
        else:
            return Response(cached_data, status=status.HTTP_200_OK)
        
    def perform_create(self, serializer):
        serializer.save()
        cache.delete(key="cities")
    
    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete(key="cities")
        cache.delete(key=f"cities_{instance.pk}")
    
    def perform_destroy(self, instance):
        pk = instance.pk
        instance.delete()
        cache.delete(key="cities")
        cache.delete(key=f"cities_{pk}")




    

