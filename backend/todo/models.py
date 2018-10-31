from django.db import models

class Todo(models.Model):
	content = models.TextField()
	done = models.BooleanField()
	due = models.DateTimeField()

	def __str__(self):
		return self.content
