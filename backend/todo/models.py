from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.TextField()
    done = models.BooleanField(default=False)
    due = models.DateTimeField()
