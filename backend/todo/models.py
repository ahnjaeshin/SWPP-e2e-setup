from django.db import models

# Create your models here.

class Todo (models.Model):
    content = models.TextField(max_length=120)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    # def introduce(self):
    #     print (self.score)

# class Team (models.Model):
#     name = models.CharField(max_length = 120)
#     leader = models.ForeignKey(
#         Hero,
#         on_delete = models.CASCADE,
#         related_name = 'leader_set',
#     )
#     members = models.ManyToManyField(
#         Hero,
#         related_name = 'teams',
#     )
#
#     def __str__(self):
#         return self.name
