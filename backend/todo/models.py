from django.db import models
from datetime import datetime
# Create your models here.
class Todo(models.Model):
	content = models.TextField()
	done = models.BooleanField(default = False)
	due = models.DateTimeField('Due', default=datetime.now())