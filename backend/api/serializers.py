from django.contrib.auth.models import User
from rest_framework import serializers


# Serializer validate username and password for us
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user