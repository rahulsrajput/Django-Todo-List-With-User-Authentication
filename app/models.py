from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    task = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.task