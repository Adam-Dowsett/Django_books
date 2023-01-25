from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("books-index")
    else:
        form = UserSignupForm()
    data = {"form": form}
    return render(request, "signup.html", data)
