from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post
from django.contrib.auth.models import User

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field="email"
    queryset=User.objects.all()
    serializer_class=UserSerializer