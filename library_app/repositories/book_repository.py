from django.db.models import Q
from .base import BaseRepository
from library_app.models import Book


class BookRepository(BaseRepository):
    model = Book

    @classmethod
    def filter_book(cls, search=None, min_price=None, max_price=None, author_id=None, genre_id=None,
                    city_author_id=None, sort=None, page=1, count_per_page=10):
        """
        Filter books based on various criteria.

        Args:
            search (str): A search query for book titles or descriptions.
            min_price (float): Minimum book price.
            max_price (float): Maximum book price.
            author_id: ID of the author of the book
            genre_id (int): ID of the Genre of the books.
            city_author_id (int): City ID of the book's author.
            sort (str): Sort the results by price (max | min).
            page (int): Page number for paginated results.
            count_per_page (int): Number of items per page in pagination.

        Returns:
            QuerySet: A filtered queryset of books.
        """
        books = Book.objects.all()
        if search:
            books = books.filter(Q(title__contains=search) | Q(description__contains=search))
        if author_id:
            books = books.filter(genre_id=author_id)
        if genre_id:
            books = books.filter(genre_id=genre_id)
        if city_author_id:
            books = books.filter(author__city__id=city_author_id)
        if min_price:
            books = books.filter(price__gte=min_price)
        if max_price:
            books = books.filter(price__lte=max_price)
        if sort:
            if sort == 'min':
                books = books.order_by('price')
            else:
                books = books.order_by('-price')
        if page:
            page = int(page)
        else:
            page = 1
        if count_per_page:
            count_per_page = int(count_per_page)
        else:
            count_per_page = 10
        return books[count_per_page * (page - 1):count_per_page * page]
