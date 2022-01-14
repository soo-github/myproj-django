from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movie.views import post_list, PostViewSet

app_name = "movie"

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("post/", post_list, name="post_list"),
    path("api/", include(router.urls)),
]