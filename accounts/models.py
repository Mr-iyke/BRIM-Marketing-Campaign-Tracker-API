from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # Add any extra fields you want for BRIM staff
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('marketer', 'Marketer'),
        ('viewer', 'Viewer'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='marketer')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username