from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import EditForm
from notes.models import Note


# Create your views here.
@login_required
def redirect_profile(request):
    return HttpResponseRedirect("/accounts/user/%s/" % request.user.username)


def profile_page(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, "accounts/profile.html", {"profile_user": profile_user, "notes": Note.objects.all()})


@login_required
def edit_profile(request):
    form = EditForm
    return render(request, "accounts/edit.html", {"form": form})
