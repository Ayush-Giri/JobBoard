from django.shortcuts import render
from rest_framework.views import APIView
from django.core.cache import cache
from skills.serializers import SkillSerializer
from skills.models import Skills
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

# Create your views here.

CACHE_TIME_TO_LIVE = 15 * 60    

class SkillView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cache_key = "skills"
        cached_data = cache.get(key=cache_key)
        if cached_data is None:
            queryset = Skills.objects.all()
            serializer = SkillSerializer(queryset, many=True)
            cache.set(key=cache_key, value=serializer.data, timeout=CACHE_TIME_TO_LIVE)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(cached_data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(user=request.user)
            cache.delete("skills")
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def patch(self, request, id):
        instance = get_object_or_404(Skills, id=id)
        if instance.user.id == request.user.id:
            serializer = SkillSerializer(instance, data=request.data, partial=True, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                cache.delete(f"skills_{id}")
                cache.delete("skills") 
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"error": "You cannot edit the skill created by another user"},
            status=status.HTTP_401_UNAUTHORIZED
        )
     
    
    def delete(self, request, id):
        if request.user.is_staff:
            instance = get_object_or_404(Skills, id=id)
            instance.delete()
            cache.delete(key=f"skills_{id}")
            cache.delete("skills") 
            return Response(
                {"message": "skill deleted successfully"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "only admin can perform this operations"},
                status=status.HTTP_401_UNAUTHORIZED
            )

