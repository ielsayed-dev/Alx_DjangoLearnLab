from django.db import models

# Step 3: Define Data Models

class Author(models.Model):
    """
    Model representing an Author.
    This model serves as the 'one' side of the one-to-many relationship.
    """
    name = models.CharField(max_length=200, help_text="The full name of the author.")

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a Book.
    This model serves as the 'many' side of the one-to-many relationship.
    It links back to an Author via a Foreign Key.
    """
    title = models.CharField(max_length=255, help_text="The title of the book.")
    publication_year = models.IntegerField(help_text="The year the book was published.")
    
    # Foreign Key relationship: one Author can have many Books.
    # related_name='books' is used by the AuthorSerializer to access related books.
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books',
        help_text="The author of this book."
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
    class Meta:
        # Ensures that sorting by year is easy when fetching books for an author
        ordering = ['publication_year']