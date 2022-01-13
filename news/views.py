import json
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from news.models import Article
# from news.serializers import ArticleAnonymousSerializer, ArticleGoldMembershipSerializer, ArticleAdminSerializer
from news.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #
    # def get_serializer_class(self):
    #     # return ArticleAnonymousSerializer
    #     # return ArticleGoldMembershipSerializer
    #     return ArticleAdminSerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #
    #     query = self.request.query_params.get("query", "")
    #     if query:
    #         qs = qs.filter(title__icontains=query)
    #
    #     year = self.request.query_params.get("year", "")
    #     if year:
    #         qs = qs.filter(created_at__year=year)
    #
    #     return qs


# article_list = RetrieveAPIView.as_view(
#     queryset=Article.objects.all(),
#     serializer_class=ArticleSerializer,
# )


# step 1
# def article_list(request):
#     qs = Article.objects.all()
#
#     # 2
#     serializer = ArticleSerializer(qs, many=True)
#     data = serializer.data
#
#     return HttpResponse(json_string, content_type="application/json")