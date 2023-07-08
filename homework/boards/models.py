from django.db import models
from users.models import User


class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title