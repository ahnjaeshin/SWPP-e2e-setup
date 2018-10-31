from django.db import models


class Todo(models.Model):
    content = models.TextField(blank=True)
    done = models.BooleanField()
    due = models.DateTimeField()

