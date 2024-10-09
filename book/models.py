from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Cover(models.TextChoices):
    hard = 'qattiq'
    soft = 'yumshoq'


class BookModel(models.Model):
    title = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(3)])
    cover_view = models.ImageField(upload_to='media', null=True, blank=True)
    author = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    description = models.TextField()
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cover = models.CharField(max_length=7, choices=Cover.choices, default=Cover.soft)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
