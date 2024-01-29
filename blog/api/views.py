from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer, CommentSerializer
from blog.models import Post, Comment
from django.contrib.auth.models import User

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    # lookup_field = ""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field="email"
    queryset=User.objects.all()
    serializer_class=UserSerializer

class CommentDetail(generics.RetrieveAPIView):
  # lookup_field=""
  queryset=Comment.objects.all()
  serializer_class = CommentSerializer