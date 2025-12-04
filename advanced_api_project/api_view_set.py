from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# ViewSet for the Author model
class AuthorViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Author instances.
    Uses AuthorSerializer, which includes nested Book data.
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

# ViewSet for the Book model
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.
    Uses BookSerializer, which includes custom validation.
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer