
from rest_framework.response import Response
from .serializers import UserSerializer, PostSerializer
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        return Response({"status":"User is Created"}, status=status.HTTP_201_CREATED)

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        return Response({"status":"Text is Posted"}, status=status.HTTP_201_CREATED)
