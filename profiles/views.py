from django.shortcuts import render, redirect
from django.http import Http404
from .models import Profile
from .forms import ProfileForm


def profile_update_view(request):
    if not request.user.is_authenticated:
        return redirect('/login?next=/profile/update/')
    user = request.user
    profile = user.profile
    form = ProfileForm(request.POST or None, instance=profile, initial={'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})
    if form.is_valid():
        profile = form.save(commit=False)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        profile.save()
    context = {
        'form': form,
        'btn_label': 'Save',
        'title': 'Update Profile'
    }
    return render(request, "profiles/form.html", context)
    

def profile_detail_view(request, username):
    profile = Profile.objects.get(user__username=username)
    if not profile:
        raise Http404
    context = {
        "username": username,
        "profile": profile
    }
    return render(request, "profiles/form.html", context)
