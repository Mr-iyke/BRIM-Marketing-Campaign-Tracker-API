from django.shortcuts import render
from rest_framework import generics, permissions, response
from .models import Campaign
from .serializers import CampaignSerializer
from clients.models import Client
from django.db import models


# Create your views here.
class CampaignListCreateView(generics.ListCreateAPIView):
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = Campaign.objects.all()
        client_id = self.request.query_params.get('client')
        status = self.request.query_params.get('status')
        if client_id:
            queryset = queryset.filter(client_id=client_id)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

     
    
class CampaignRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    

class ClientReportView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return response.Response({"error": "Client not found"}, status=404)

        campaigns = Campaign.objects.filter(client=client)

        data = {
            "client_id": client.id,
            "client_name": client.name,
            "total_campaigns": campaigns.count(),
            "active_campaigns": campaigns.filter(status='active').count(),
            "completed_campaigns": campaigns.filter(status='completed').count(),
            "total_budget": campaigns.aggregate(models.Sum('budget'))['budget__sum'] or 0.0,
        }
        return response.Response(data)

