from django.shortcuts import render
from book.models import BookModel
from book.forms import BookForm
# Create your views here.


def books_list_view(request):
    books = BookModel.objects.all()
    context = {'books': books}
    return render(request, 'books_list.html', context)


def books_detail_view(request, pk):
    book = BookModel.objects.get(pk=pk)
    if book:
        context = {'book': book}
        return render(request, 'books_detail.html', context)
    return render(request, '404.html')


def create_book_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            BookModel.objects.create(
                title=form.cleaned_data['title'],
                cover_view=form.cleaned_data['cover_view'],
                author=form.cleaned_data['author'],
                description=form.cleaned_data['description'],
                pages=form.cleaned_data['pages'],
                price=form.cleaned_data['price'],
                cover=form.cleaned_data['cover'],
            )
        return render(request, 'form.html')
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'form.html', context)


