from rest_framework import viewsets
from .models import Book
from .serializers import *


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = bookserializer
