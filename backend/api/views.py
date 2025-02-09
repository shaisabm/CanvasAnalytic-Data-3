from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, SampleDataSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import SampleData

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class GetSampleData(generics.ListAPIView):
    serializer_class = SampleDataSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return SampleData.objects.all()






