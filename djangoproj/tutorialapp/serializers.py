from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tutorialapp.models import Step


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StepSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=4)
    text = serializers.CharField()
    completed = serializers.BooleanField(default=False)
    class Meta:
        model = Step
        fields = ['name', 'number', 'text', 'completed']