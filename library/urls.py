from django.conf.urls import url
from . import views

app_name = 'library'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^books/$', views.BooksView.as_view(), name='books'),
    url(r'^authors/$', views.AuthorsView.as_view(), name='authors'),

    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='author-details'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'books/add/$', views.BookCreate.as_view(), name='book-add'),
    url(r'authors/add/$', views.AuthorCreate.as_view(), name='author-add'),

    url(r'books/update/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name='book-update'),
    url(r'authors/update/(?P<pk>[0-9]+)/$', views.AuthorUpdate.as_view(), name='author-update'),

    url(r'books/(?P<pk>[0-9]+)/delete$', views.BookDelete.as_view(), name='book-delete'),
    url(r'authors/(?P<pk>[0-9]+)/delete$', views.AuthorDelete.as_view(), name='author-delete'),
]