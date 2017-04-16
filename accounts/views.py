from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
def profile_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'profile_user': user})
