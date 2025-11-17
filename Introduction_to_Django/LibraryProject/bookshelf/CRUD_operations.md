# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Expected Output <Book: 1984>

# Retrieve Operation

# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
books.save()
book

# Update Operation

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

# Expected Output <Book: Nineteen Eighty-Four>


# Delete Operation

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# Ecpected Outage <QuerySet []>


