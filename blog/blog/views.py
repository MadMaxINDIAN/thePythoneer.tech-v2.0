from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from json import dumps
from django.contrib.auth.decorators import login_required
from blog_app.forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(req):
    blogs = BlogPost.objects.all()
    data = {
        'title': "Home",
        'blog': "thePythoneer.tech",
        'blogs': blogs,
        'authenticated' : req.user.is_authenticated
    }
    return render(req, 'home.html', data)
