# Generated by Django 4.0.2 on 2022-02-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmany', '0004_alter_author_2_books_alter_book_2_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_2',
            name='books',
            field=models.ManyToManyField(to='bookmany.Book_2'),
        ),
        migrations.AlterField(
            model_name='book_2',
            name='authors',
            field=models.ManyToManyField(to='bookmany.Author_2'),
        ),
    ]
