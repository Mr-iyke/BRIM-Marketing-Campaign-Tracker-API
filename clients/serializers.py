from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'address', 'added_by', 'created_at']
        read_only_fields = ['added_by', 'created_at']