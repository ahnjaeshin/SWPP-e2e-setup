from django.db import models


class Todo(models.Model):
	content = models.TextField()
	done = models.BooleanField(default=False)