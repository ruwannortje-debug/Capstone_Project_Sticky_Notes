"""Database models for the sticky notes application."""

from django.db import models


class Note(models.Model):
    """Store a single sticky note entry."""

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the note title for the admin and shell."""
        return self.title
