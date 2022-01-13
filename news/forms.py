from django import forms
from news.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title:
            if len(title) < 3:
                raise forms.ValidationError("3글자 이상!!")
        return title
