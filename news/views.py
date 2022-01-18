import json
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from news.models import Article
# from news.serializers import ArticleAnonymousSerializer, ArticleGoldMembershipSerializer, ArticleAdminSerializer
from news.serializers import ArticleSerializer

# list, detail, create, update, deletd를 1개 Viewset에서 지원

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [AllowAny]  # DRF 디폴트 설정
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # if self.request.method in("POST", "PUT", "PATCH", "DELETE"):
            # return [IsAuthenticated()]
        # return [AllowAny()]

        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # 유효성 검사가 끝나고 나서
    # 실제 serializer.save()를 할 때 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않습니다.
        # 대신 키워드 인자를 통한 속성 지정을 지원합니다.
        serializer.save(author=self.request.user)

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