from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

class Issue(models.Model):
    """Model for tracking municipal service issues"""
    
    # Issue type choices
    ISSUE_TYPES = [
        ('Water', 'Water Services'),
        ('Electricity', 'Electricity'),
        ('Roads', 'Roads & Transport'),
        ('Waste', 'Waste Management'),
        ('Other', 'Other Municipal Issue'),
    ]
    
    # Status choices
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    # User relationship - each issue belongs to a user
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='reported_issues'
    )
    
    # Tracking ID - using formatted string for readability
    tracking_id = models.CharField(max_length=50, unique=True, blank=True)
    
    # Issue details
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20, blank=True, null=True, help_text="Optional contact number for follow-up")
    
    # Status tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """Override save to generate formatted tracking ID if not present"""
        if not self.tracking_id:
            # Generate formatted tracking ID: GTS-YYYYMM-XXXXXX
            # Example: GTS-202403-A1B2C3
            date_part = datetime.now().strftime('%Y%m')
            random_part = uuid.uuid4().hex[:6].upper()
            self.tracking_id = f"GTS-{date_part}-{random_part}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        """String representation of the issue"""
        return f"{self.tracking_id} - {self.issue_type} - {self.user.username}"
    
    class Meta:
        ordering = ['-created_at']  # Show newest issues first
        verbose_name = "Service Issue"
        verbose_name_plural = "Service Issues"