from django.http import JsonResponse
from .services.book_service import BookService
from .serializers import BookSerializer
from rest_framework.views import APIView


class GetBookList(APIView):
    def get(self, request):
        books = BookService().all_book()
        data = BookSerializer(books, many=True).data
        return JsonResponse(data, safe=False)


class GetBook(APIView):
    def get(self, request, pk):
        book = BookService().get_book(pk)
        data = BookSerializer(book).data
        return JsonResponse(data)


class CreateBook(APIView):
    def post(self, request):
        book = BookService().create_book(title=request.POST.get('title'), author_id=request.POST.get('author'),
                                         genre_id=request.POST.get('genre'), publishDate=request.POST.get('publishDate'), ISBN=request.POST.get('ISBN'), price=request.POST.get('price'))
        return JsonResponse(BookSerializer(book).data)


class UpdateBook(APIView):
    def put(self, request, pk):
        book = BookService().update_book(pk, **request.data)
        return JsonResponse(BookSerializer(book).data)


def filter_book(request):
    books = BookService().filter_book(
        search=request.GET.get('search'),
        min_price=request.GET.get('min_price'),
        max_price=request.GET.get('max_price'),
        author_id=request.GET.get('author'),
        genre_id=request.GET.get('genre'),
        city_author_id=request.GET.get('city_author'),
        sort=request.GET.get('sort'),
        page=request.GET.get('page'),
        count_per_page=request.GET.get('count_per_page'))
    return JsonResponse(BookSerializer(books, many=True).data, safe=False)
