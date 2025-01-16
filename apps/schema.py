# import graphene
# from graphene_django.types import DjangoObjectType
# from apps.models import Book
#
#
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = ("id", "title", "author")
#
#
# class Query(graphene.ObjectType):
#     all_books = graphene.List(BookType)
#     book_by_id = graphene.Field(BookType, id=graphene.String())
#
#     def resolve_all_books(root, info):
#         return Book.objects.all()
#
#     def resolve_book_by_id(root, id):
#         return Book.objects.get(id=id)
#
#
# class AddBookMutation(graphene.Mutation):
#     class Arguments:
#         title = graphene.String(required=True)
#         author = graphene.String(required=True)
#
#     book = graphene.Field(BookType)
#
#     def mutate(self, info, title, author):
#         book = Book.objects.create(title=title, author=author)
#         return AddBookMutation(book=book)
#
#
# class Mutation(graphene.ObjectType):
#     add_book = AddBookMutation.Field()
#
#
# schema = graphene.Schema(query=Query)

import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay
from apps.models import Book, Author


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "author")


class BookConnection(relay.Connection):
    class Meta:
        node = BookType


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book_by_id = graphene.Field(BookType, id=graphene.String())
    search_books = graphene.List(BookType, title=graphene.String(), author=graphene.String())

    def resolve_all_books(self, info, first=None, after=None):
        query = Book.objects.all()
        return BookConnection.from_queryset(query, info, first=first, after=after)

    def resolve_book_by_id(self, info, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            return None

    def resolve_search_books(self, info, title=None, author=None):
        books = Book.objects.all()
        if title:
            books = books.filter(title__icontains=title)
        if author:
            books = books.filter(author__icontains=author)
        return books

    def resolve_book_by_id_with_author(self, info, id):
        try:
            book = Book.objects.get(id=id)
            return {
                'book': book,
                'author': book.author
            }
        except Book.DoesNotExist:
            return None


class AddBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)

    book = graphene.Field(BookType)
    errors = graphene.List(graphene.String)

    def mutate(self, info, title, author):
        errors = []

        if not title:
            errors.append("Sarlavha kiritilmadi.")
        if not author:
            errors.append("Muallif kiritilmadi.")

        if errors:
            return AddBookMutation(errors=errors)

        book = Book.objects.create(title=title, author=author)
        return AddBookMutation(book=book, errors=errors)


class Mutation(graphene.ObjectType):
    add_book = AddBookMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
