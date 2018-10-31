from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):
    content = models.TextField()
    done = models.BooleanField()
    due = models.DateTimeField(null=True)
