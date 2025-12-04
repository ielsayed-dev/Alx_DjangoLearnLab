from django.contrib import admin
from .models import Author, Book

# Register models to make them available in the Django Admin interface for easy testing.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')
    list_filter = ('publication_year', 'author')
    search_fields = ('title',)
    raw_id_fields = ('author',) # Use raw ID input for Foreign Key for better performance