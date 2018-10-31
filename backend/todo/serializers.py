from rest_framework import serializers
from .models import Todo

class ToDoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('content', 'done', 'due')