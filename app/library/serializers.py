from rest_framework import serializers
from .models import Readers, Books, Readerbooks


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'author')


class ReaderBooksSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='book.title')
    author = serializers.ReadOnlyField(source='book.author')

    class Meta:
        model = Readerbooks
        fields = ('id', 'title', 'author')


class ReaderSerializer(serializers.ModelSerializer):
    books = ReaderBooksSerializer(source='readerbooks_set', many=True, required=False)

    class Meta:
        model = Readers
        fields = ['id', 'first_name', 'last_name', 'books']

