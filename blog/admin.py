from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text', 'published', 'pub_date')

admin.site.register(Comment)
