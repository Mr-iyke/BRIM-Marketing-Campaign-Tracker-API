from django.urls import path
from .views import CampaignListCreateView, CampaignRetrieveUpdateDeleteView, ClientReportView

urlpatterns = [
    path('campaigns/', CampaignListCreateView.as_view(), name='campaign-list-create'),
    path('campaigns/<int:pk>/', CampaignRetrieveUpdateDeleteView.as_view(), name='campaign-detail'),
    path('clients/<int:pk>/report/', ClientReportView.as_view(), name='client-report'),
]
