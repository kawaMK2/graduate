from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Tag, Note
from accounts.models import User


# Create your views here.
def top(request):
    return render(request, "notes/top.html", {"users": User.objects.all(), "tags": Tag.objects.all()})


def note(request, note_title):
    current_note = get_object_or_404(Note, title=note_title)
    return render(request, "notes/note.html", {"note": current_note})


def tag(request, tag_id):
    current_tag = get_object_or_404(Tag, id=tag_id)
    return render(request, "notes/tag.html", {"tag": current_tag, "notes": Note.objects.all()})
