from django.db import models


class Todo(models.Model):
    content = models.TextField(null=True, blank=True)
    done = models.BooleanField()
    due = models.DateTimeField()

    