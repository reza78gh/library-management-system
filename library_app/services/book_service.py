from library_app.repositories.book_repository import BookRepository


class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def all_book(self):
        return self.repository.all()

    def get_book(self, book_id):
        return self.repository.get(book_id)

    def create_book(self, **kwargs):
        return self.repository.create(**kwargs)

    def update_book(self, book_id, **kwargs):
        book = self.repository.get(book_id)
        return self.repository.update(book, **kwargs)

    def filter_book(self, **kwargs):
        return self.repository.filter_book(**kwargs)
