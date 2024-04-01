from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer, CommentSerializer, TagSerializer
from blog.models import Post, Comment, Tag
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import viewsets, generics

from rest_framework.decorators import action
from rest_framework.response import Response

"""
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    # lookup_field = ""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
"""
# Convert to viewsets
class PostViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticatedOrReadOnly]
  queryset = Post.objects.all()

  def get_serializer_class(self):
    if self.action in ("list", "create"):
      return PostSerializer
    return PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field="email"
    queryset=User.objects.all()
    serializer_class=UserSerializer

class CommentDetail(generics.RetrieveAPIView):
  # lookup_field=""
  queryset=Comment.objects.all()
  serializer_class = CommentSerializer

# viewsets
class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

  # Retrieve posts with the specific tag
  @action(methods=["get"], detail=True, name="Posts with the Tag")
  def posts(self, request, pk=None):
      tag = self.get_object()
      post_serializer = PostSerializer(
          tag.posts, many=True, context={"request": request}
      )
      return Response(post_serializer.data)