from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogposts = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogposts': blogposts})

def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blogdetail' : blogdetail})