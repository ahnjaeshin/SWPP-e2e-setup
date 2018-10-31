from django.db import models


class ToDo(models.Model):
	content = models.CharField(max_length=120)
	done = models.BooleanField(default=False)