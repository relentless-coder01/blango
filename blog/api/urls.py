from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken import views
from blog.api.views import PostList, PostDetail, UserDetail, CommentDetail

# Swagger UI
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    path("comments/<int:pk>", CommentDetail.as_view(), name="api_comment_detail"),
]

urlpatterns += [
    # re_path(
    #     r"^swagger(?P<format>\.json|\.yaml)$",
    #     schema_view.without_ui(cache_timeout=0),
    #     name="schema-json",
    # ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

# To allow formatting options in browser
# Eg. posts/4.json
urlpatterns = format_suffix_patterns(urlpatterns)