from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse

from .models import Post
from .forms import CommentsForm

# Create your views here.


def view_posts(request):
    blog_list = Post.objects.all().filter(published=True).order_by('-published_date')
    context = {
        'posts': blog_list
    }

    return render(request, 'blog/blog_list.html', context)



def post_detail(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    form = CommentsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           form.instance.user = request.user
           form.instance.post = posts
           form.save()
           return redirect(reverse('blog:post_detail', args=[posts.id]))
        #    return redirect('post_detail', post_id=post_id)


    context = {
        'post': posts,
        'form': form
    }

    return render(request, 'blog/blog_detail.html', context)

