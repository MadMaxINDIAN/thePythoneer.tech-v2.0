from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from json import dumps
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .decorators import *
from django.contrib.auth import authenticate, login, logout
from django.conf import settings 
from django.core.mail import send_mail 
from django.template.loader import render_to_string


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
            user = User.objects.get(username=user)
            Profile(id=user.id, user=user).save()
            messages.success(req, "Account has been created for " + user.username)
            
            # SENDING MAIL TO THE USER
            subject = 'Welcome to thePythoneer world'
            message = f'Hi {user.username}, thank you for registering in thePythoneer.tech.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ] 
            send_mail( subject, message, email_from, recipient_list )

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
            subject = 'Welcome to thePythoneer world'
            message = f'Hi {user.username}, thank you for registering in thePythoneer.tech.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list, html_message=render_to_string("register-mail.html", {'username': req.user.username}))
            return redirect("/")
        else:
            messages.info(req, "Username or Password is incorrect")
    return render(req,"login_user.html",data)

@login_required(login_url="/u/login_user")
def profile(req,id):
    try:
        pro = Profile.objects.get(id=id)
    except:
        return render(req, "user_not_found.html")
    context = {
        'user': pro.user,
        'img': pro.image,
        'author': pro.author,
        'profile': pro
    }
    return render(req, "page-user.html", context)

def logout_user(req):
    logout(req)
    return redirect("/u/login_user")