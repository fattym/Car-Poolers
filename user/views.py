from django.shortcuts import render,redirect

# Create your views here.
rom django.http import HttpResponse, Http404
from .forms import SignupForm, ImageForm, CommentForm, ProfileForm
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

from django.template.loader import render_to_string
from .models import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})


