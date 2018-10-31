from django.db import models


class Todo(models.Model):
    content = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    due = models.DateTimeField(auto_now_add=True)
