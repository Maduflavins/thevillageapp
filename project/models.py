from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    avatar = CloudinaryField('avatar')
    title = models.CharField(max_length=100)
