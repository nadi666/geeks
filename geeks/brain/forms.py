from django import forms
from django.conf import settings
from .models import Task
from rest_framework import serializers

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'