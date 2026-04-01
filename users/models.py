from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime


class Issue(models.Model):
    ISSUE_TYPES = [
        ('Water', 'Water Services'),
        ('Electricity', 'Electricity'),
        ('Roads', 'Roads & Transport'),
        ('Waste', 'Waste Management'),
        ('Other', 'Other Municipal Issue'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    tracking_id = models.CharField(max_length=50, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues')
    
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 🔥 AUTO GENERATE TRACKING ID
    def save(self, *args, **kwargs):
        if not self.tracking_id:
            self.tracking_id = f"GTS-{datetime.now().strftime('%Y%m')}-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tracking_id} - {self.issue_type} - {self.user.username}"
    
    class Meta:
        ordering = ['-created_at']