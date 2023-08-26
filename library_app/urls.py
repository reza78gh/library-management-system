from django.urls import path
from .views import *

urlpatterns = [
    path('book/list/', GetBookList.as_view()),
    path('book/<int:pk>/', GetBook.as_view()),
    path('book/create/', CreateBook.as_view()),
    path('book/update/<int:pk>/', UpdateBook.as_view()),
    path('book/filter/', filter_book),
]
