from django.db import models


class Todo(models.Model):
    content = models.TextField(default="")
    done = models.BooleanField()
