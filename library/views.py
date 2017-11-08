from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import loader
from django.http import HttpResponse
from .models import Book, Author

def index(request):
    template = loader.get_template('library/index.html')
    return HttpResponse(template.render())


class BooksView(generic.ListView):
    template_name = 'library/books.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()


class AuthorsView(generic.ListView):
    template_name = 'library/authors.html'
    context_object_name = 'all_authors'

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'library/author_details.html'


class DetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_details.html'


class BookCreate(CreateView):
    model = Book
    fields = ['title','author', 'cover', 'genre']


class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name','last_name']


class BookUpdate(UpdateView):
    model = Book
    fields = ['title','author', 'cover', 'genre']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('library:authors')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('library:books')
