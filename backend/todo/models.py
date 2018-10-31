from django.db import models


class Todo (models.Model):
    content = models.CharField(max_length = 120)
    done = models.BooleanField(default = False)
    #due = models.DateTimeField(auto_now_add=True)


