from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    @swagger_auto_schema(request_body=UserSerializer, operation_id="Create user")
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_id="Delete user")
    def delete(self, request):
        user = User.objects.filter(username=request.data.get('username')).first()
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)