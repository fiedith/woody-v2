from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Board, Comment
from .serializers import BoardSerializer, CommentSerializer
from users.models import User


# ALL POSTS
class BoardListView(APIView):
    # GET ALL POSTS
    @swagger_auto_schema(operation_id="Get posts")
    def get(self, request):
        boards = Board.objects.all()
        # many = True to get many objects
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)


# INDIVIDUAL POSTS
class BoardView(APIView):
    # CREATE POST
    @swagger_auto_schema(request_body=BoardSerializer, operation_id="Create post")
    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        # check validation
        if serializer.is_valid():
            # get user with corresponding id
            author_id = serializer.validated_data.get('author').id
            author_exists = User.objects.filter(id=author_id).exists()
            # if user with corresponding id exists, save author id as author_id field
            if author_exists:
                serializer.save(author_id=author_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Author does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE POST
    @swagger_auto_schema(operation_id="Delete post")
    def delete(self, request, pk=None):
        try:
            board = Board.objects.get(pk=pk)
            board.delete()
            # 204 status code = delete successful
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Board.DoesNotExist:
            return Response({'message': 'Board not found.'}, status=status.HTTP_404_NOT_FOUND)


# COMMENTS VIEW
# requirements: comments should provide all CRUD
# in this case, viewsets provides APIs for all CRUD
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id if self.request.user.is_authenticated else None)