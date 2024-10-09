from modeltranslation.translator import TranslationOptions, register
from book.models import BookModel


@register(BookModel)
class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'author', 'description')