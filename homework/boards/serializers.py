from rest_framework import serializers
from .models import Board, Comment
from users.models import User

from users.serializers import UserSerializer


# posts
class BoardSerializer(serializers.ModelSerializer):
    # take user's id
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Board
        fields = ['id', 'title', 'content', 'author', 'comments']

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', None)
        board = Board.objects.create(**validated_data)
        if comments_data:
            for comment_data in comments_data:
                Comment.objects.create(board=board, **comment_data)
        return board

    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comments', None)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        if comments_data:
            instance.comments.all().delete()
            for comment_data in comments_data:
                Comment.objects.create(board=instance, **comment_data)
        return instance


# comments
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'context', 'board', 'author']

    def create(self, validated_data):
        comment = Comment.objects.create(
            context=validated_data['context'],
            board=validated_data['board'],
            author=validated_data['author']
        )
        return comment