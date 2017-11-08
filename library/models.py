# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('library:author-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    cover = models.FileField()

    def get_absolute_url(self):
        return reverse('library:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' by ' + self.author.first_name + ' ' + self.author.last_name
