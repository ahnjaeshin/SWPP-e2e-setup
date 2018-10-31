from django.db import models
import json
# Create your models here.
class Todo(models.Model):
    content = models.TextField()
    done = models.BooleanField(default=False)
