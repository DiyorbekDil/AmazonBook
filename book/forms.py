from django import forms
from book.models import BookModel
from django.core.validators import MinLengthValidator


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ('title', 'cover_view', 'author', 'description', 'pages', 'price', 'cover')