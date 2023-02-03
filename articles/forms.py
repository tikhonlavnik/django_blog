from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from articles.models import Article


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category isn't chosen"

    class Meta:
        model = Article
        exclude = ['slug', 'user']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form_textarea'}),
        }
