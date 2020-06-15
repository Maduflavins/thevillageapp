from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Project

# Create your views here.

@login_required
def product_upload(request):
    instance = (Project)
    if request.method == "post":
        form = ProductForm(request.post, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/project/projects.html')
    form = ProductForm()
    return render(request, 'project/projects.html', {'form':form})


def display_products(request):
    project_list = Project.objects.all()
    context = {
        'products': project_list,
    }
    return render(request, 'project/project_list.html', context)

