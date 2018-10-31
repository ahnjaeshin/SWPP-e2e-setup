from django.db import models
from django.utils import timezone

class Todo(models.Model):
    content = models.TextField(max_length=120)
    done = models.BooleanField(default=False)
    due = models.DateTimeField(default=timezone.now)
