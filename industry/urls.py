from rest_framework.routers import DefaultRouter
from industry.views import IndustryViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r'industries', IndustryViewset)

urlpatterns = [
    path('', include(router.urls))
]