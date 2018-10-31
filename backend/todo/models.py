from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    content = models.TextField()
    done = models.BooleanField()
    def __str__(self):
        return self.content
