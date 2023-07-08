from rest_framework import serializers
from .models import Board
from users.models import User


class BoardSerializer(serializers.ModelSerializer):
    # take user's id
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Board
        fields = ['id', 'title', 'content', 'author']