from django.db import models


class Todo(models.Model):
    content = models.TextField(max_length=240)
    done = models.BooleanField()
