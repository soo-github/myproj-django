from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from movie.models import Post
from movie.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_list(request):
    qs = Post.objects.all()
    data = [
        {"id": post.id,
         "title": post.title,
         "poster": post.poser,
         "story": post.story}
        for post in qs
    ]