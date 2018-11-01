from django.db import models


class Todo(models.Model):
    content = models.TextField(null=False)
    done = models.BooleanField(default=False)
    # due = models.DateTimeField()
