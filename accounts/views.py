from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
def redirect_profile(request):
    return HttpResponseRedirect("/accounts/%s/" % request.user.username)


def profile_page(request, username):
    login_user = request.user
    profile_user = get_object_or_404(User, username=username)
    return render(request, "profile.html", {"profile_user": profile_user, "login_user": login_user})
