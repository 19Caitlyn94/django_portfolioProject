from django.shortcuts import render
from .models import Blog

def allblogs(request):
    blogposts = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogposts': blogposts})