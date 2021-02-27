from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Login",
        "title": "Login"
    }
    return render(request, "accounts/auth.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    context = {
        "confirmation": "Are you sure?",
        "btn_label": "Confirm",
        "title": "Logout"
    }
    return render(request, "accounts/auth.html", context)


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        return redirect("/login/")
    context = {
        "form": form,
        "btn_label": "Sign Up",
        "title": "Registration"
    }
    return render(request, "accounts/auth.html", context)

