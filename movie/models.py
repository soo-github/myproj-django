from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    title = models.CharField(max_length=100, db_index=True, validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="한글을 한 글자 이상 입력해주세요."),
                             ])
    poster = models.ImageField(blank=True)
    story = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title
