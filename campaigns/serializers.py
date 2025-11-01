from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id', 'client', 'campaign_name', 'campaign_type', 
            'start_date', 'end_date', 'budget', 'status', 'created_at'
        ]
        read_only_fields = ['created_at']
        client_name = serializers.CharField(source='client.name', read_only=True)

