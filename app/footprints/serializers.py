from rest_framework import serializers
from .models import Lifestyle, Choice, UserChoice


class LifestyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifestyle
        fields = ('id', 'name')


class ChoiceSerializer(serializers.ModelSerializer):
    lifestyle = LifestyleSerializer(read_only=True)

    class Meta:
        model = Choice
        fields = ('id', 'name', 'carbon', 'lifestyle')


class UserChoiceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    choice = ChoiceSerializer(read_only=True)

    class Meta:
        model = UserChoice
        fields = ('id', 'user', 'choice')
