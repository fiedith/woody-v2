from django.db import models
from users.models import User

# posts
class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

# comments
class Comment(models.Model):
    context = models.CharField(max_length=255)
    # requirement: comments should cascade with board
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    # requirement: comments should also cascade with user
    author = models.IntegerField(null=True)

    def __str__(self):
        return self.context