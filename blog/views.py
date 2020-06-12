from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import BlogPost
from .forms import CommentForm


class BlogPostListView(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(published=True)
    template_name = 'blog/list.html'
    context_object_name = 'blog_posts'
    paginate_by = 15  # that is all it takes to add pagination in a Class Based View


class BlogPostDetailView(DetailView):
    model = BlogPost
    queryset = BlogPost.objects.filter(published=True)
    template_name = 'blog/detail.html'
    context_object_name = 'blog_post'


def add_comment(request, slug):
    post = BlogPost.objects.filter(published=True)
    if request.method == 'POST':
        form = CommentForm(requst.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog/detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'blog/add_comment.html'
    context =  {'form': form}
    return render(request, template, context)
