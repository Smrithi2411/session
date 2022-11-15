from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from sessionapp.forms import Login


def email_login(request):
    if "email" in request.session:
        return redirect("profile")
    if request.method == "GET":
        form = Login()
    else:
        form = Login(request.POST)
        if form.is_valid():
            request.session["email"] = form.cleaned_data["email"]
            request.session["fullName"] = form.cleaned_data["fullName"]
            request.session["Gender"] = form.cleaned_data["Gender"]
            request.session["age"] = form.cleaned_data["age"]
            return redirect("profile")
    return render(request, "core/login.html", {"form": form})

def profile(request):
    return render(request, "core/profile.html")

def logout(request):
    request.session.pop("email")
    return HttpResponse("Logged out!")