from django.db import models

class Todo(models.Model):
    content = models.TextField(max_length=140)
    done = models.BooleanField(default=False)
    due = models.DateTimeField(auto_now=True)