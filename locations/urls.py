from rest_framework.routers import DefaultRouter
from locations.views import CountryViewset, CityViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r'countries', CountryViewset)
router.register(r'cities', CityViewset)

urlpatterns = [
    path('', include(router.urls))
]