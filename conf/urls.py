from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from book.views import create_book_view


urlpatterns = []


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('book.urls', namespace='book')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
