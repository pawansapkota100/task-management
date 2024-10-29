from django.db import models
from django.contrib.auth import get_user_model

user=get_user_model()

# Create your models here.
class Task(models.Model):
    priority=[
        ("L", "Low"),
        ("M","Medium"),
        ("H","High"),
    ]
    status=[
        ("P","Pending"),
        ("I","InProcess"),
        ("C","Completed"),
    ]
    name= models.CharField(max_length=150, blank=False, null=False)
    description= models.CharField(max_length=250, blank=True, null=True)
    created_by=models.ForeignKey(user, on_delete=models.CASCADE)
    priority= models.CharField(max_length=1, choices=priority, default="M")
    status= models.CharField(max_length=1, choices=status, default="P")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name