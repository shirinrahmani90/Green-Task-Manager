from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    High = 'H'
    Medium = 'M'
    Low = 'L'
    IMPACT_CHOICES = [
        (High, 'High Impact on the Environment'),
        (Medium, 'Medium Impact on the Environment'),
        (Low, 'Low Impact on the Environment'),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=250, null=True, blank=True)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    sustainability_rating = models.PositiveIntegerField(null=True, blank=True)
    energy_consumption = models.CharField(max_length=1, choices=IMPACT_CHOICES, default=High)
    carbon_footprint = models.CharField(max_length=1, choices=IMPACT_CHOICES, default=High)
    water_usage = models.CharField(max_length=1, choices=IMPACT_CHOICES, default=High)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['complete']


