from django.shortcuts import render
import uuid
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from authorisation.decorators import *
from .forms import *

def uniqueidgenerator():
    x = uuid.uuid4().int >> 64
    if x < 9223372036854775807:
        return x
    else:
        return uniqueidgenerator()

# Create your views here.
# # # # # # # # # # # # # # # # # # # # #    BLOG SECTION    # # # # # # # # # # # # # # # # # # # # # 
# api => "/b/<str:blog_title>"
# request => GET, POST
# returns => blog post with title = blog_title
def blog(req,blog_title):
    if blog_title == 'dashboard':
        return dashboard(req)
    blog = BlogPost.objects.filter(title=blog_title)[0]
    tags = blog.tags.all()
    feedback_form = FeedbackForm(instance=blog)
    if req.method == 'POST':
        
        blog = BlogPost.objects.filter(title=blog_title)[0]
        blog.feedback_amazed += int(req.POST['feedback_amazed'])
        blog.feedback_loved += int(req.POST["feedback_loved"])
        blog.feedback_upvote += int(req.POST['feedback_upvote'])
        blog.save()
        res = {
            'feedback_amazed': blog.feedback_amazed,
            'feedback_loved': blog.feedback_loved,
            'feedback_upvote': blog.feedback_upvote,
        }
        return JsonResponse(res)
    return render(req, 'blog.html',{'title': blog.title,'blog': "thePythonner.tech",'post': blog,'tags': tags, 'feedback_form': feedback_form, 'authenticated': req.user.is_authenticated})


# api => "/b/create_blog"
# request => GET, POST
# returns => Create a new Blog POST
@login_required(login_url="/u/login_user")
@allowed_user(allowed_roles=['Editor'])
def create_blog(req):
    form = BlogPostForm(initial={'id': uniqueidgenerator()})
    context = {
        'form': form
    }
    if req.method == 'POST':
        form = BlogPostForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(req, 'create_blog.html',{'title': "Create Blog Post",'blog': "thePythonner.tech", 'form': form, 'authenticated': req.user.is_authenticated})


# api => "/b/dashboard"
# request => GET, POST
# returns => Editor Dashboard
# @login_required(login_url="/u/login_user")
# @allowed_user(allowed_roles=['Editor'])
def dashboard(req):
    return render(req, 'dashboard.html')


# api => "/b/update_blog/<str:title>"
# request => GET, POST
# returns => Update Blog POST
@login_required(login_url="/")
@allowed_user(allowed_roles=['Editor'])
def update_blog(req, title):
    blog = BlogPost.objects.filter(title=title)[0]
    form = BlogPostForm(instance=blog)
    context = {
        'form': form
    }
    if req.method == 'POST':
        form = BlogPostForm(req.POST, req.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(req, 'create_blog.html',{'title': "Create Blog Post",'blog': "thePythonner.tech", 'form': form,  'authenticated': req.user.is_authenticated})
