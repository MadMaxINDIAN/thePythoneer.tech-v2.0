from django.db import models
from django.contrib.auth.models import User
from blog_app.models import Author
import uuid

# Create your models here.
class Profile(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.id)
    
