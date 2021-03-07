# IMPORTS
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home),
    # path('b/comment/<str:blog_title>', views.comment),
    # path('b/create_blog', views.create_blog),
    # path('b/update_blog/<str:title>', views.update_blog),
    # path('b/<str:blog_title>', views.blog),
    path('create_user', views.create_user),
    path('login_user', views.login_user),
    path('logout_user', views.logout_user),
    path('profile/<str:id>', views.profile),
]