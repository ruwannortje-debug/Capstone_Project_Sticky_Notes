"""View functions for the sticky notes application."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Display all saved notes on the home page."""
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    """Display a single note by primary key."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """Create a new note from submitted form data."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """Update an existing note selected by primary key."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """Delete a note and return to the list view."""
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
