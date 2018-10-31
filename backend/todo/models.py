from django.db import models

class Todo(models.Model):
    content = models.CharField(max_length = 120)
    done = models.BooleanField(default = False)


# Create your models here.
