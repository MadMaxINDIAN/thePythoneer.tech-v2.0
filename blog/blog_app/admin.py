from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(EmailIPLocator)
admin.site.register(Tag)
admin.site.register(BlogPostComment)