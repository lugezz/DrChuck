from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author', through='Authored')

    def __str__(self) -> str:
        return f'{self.title.title()}' # Author?

class Author(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField('Book', through='Authored')

    def __str__(self) -> str:
        return self.name.title()

class Authored(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} - {self.author.name}'

# Sin el authored - Da error porque uno necesita el otro y viceversa
class Book_2(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author_2')

    def __str__(self) -> str:
        return f'{self.title.title()}' # Author?


class Author_2(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField('Book_2')

    def __str__(self) -> str:
        return self.name.title()