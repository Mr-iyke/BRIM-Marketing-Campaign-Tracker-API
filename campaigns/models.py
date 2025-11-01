from django.db import models
from django.db import models
from clients.models import Client

# Create your models here.
class Campaign(models.Model):
    CAMPAIGN_TYPE_CHOICES = [
        ('email', 'Email Marketing'),
        ('social', 'Social Media'),
        ('ads', 'Digital Ads'),
        ('sms', 'SMS/WhatsApp'),
        ('content', 'Content Marketing'),
    ]

    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='campaigns')
    campaign_name = models.CharField(max_length=100)
    campaign_type = models.CharField(max_length=50, choices=CAMPAIGN_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.campaign_name} for {self.client.name}"