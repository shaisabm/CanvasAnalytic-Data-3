from django.contrib.auth.models import User
from rest_framework import serializers
from .models import SampleData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SampleDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SampleData
        fields = ['id',
                  'feature1',
                  'feature2',
                  'feature3',
                  'feature4',
                  'feature4',
                  'feature5',
                  'feature6',
                  'feature7',
                  'feature8',
                  'feature9',
                  'feature10']
