from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from json import dumps
from django.contrib.auth.decorators import login_required
from .forms import *
from .decorators import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# # # # # # # # # # # # # # # # # # # # #    USER SECTION    # # # # # # # # # # # # # # # # # # # # # 
@unauthenticted_user_only
def create_user(req):
    print(req.POST.get('next',""))
    if req.user.is_authenticated:
        return redirect("/")
    errors = {}
    form = CreateUser()
    if req.method == "POST":
        form = CreateUser(req.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(req, "Account has been created for " + user)
            return redirect("/u/login_user")
        else:
            for key in form.errors:
                errors[key] = form.errors[key][0]
    data = {
        'form': form,
        'errors': errors,
        'data': req.POST
    }
    return render(req,"register_user.html",data)

@unauthenticted_user_only
def login_user(req):
    if req.user.is_authenticated:
        return redirect("/")
    data = {}
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect("/")
        else:
            messages.info(req, "Username or Password is incorrect")
    return render(req,"login_user.html",data)

def logout_user(req):
    logout(req)
    return redirect("/u/login_user")