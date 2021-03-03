from django.forms import ModelForm
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

class FeedbackForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['feedback_upvote','feedback_loved','feedback_amazed']
