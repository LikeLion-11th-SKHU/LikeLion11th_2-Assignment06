from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.utils import timezone
from .models import Blog 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = BlogForm
        return render(request, 'create.html', {'form' : form})

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'read.html', {'blogs' : blogs}) 

def detail(request, id):  
    blog = get_object_or_404(Blog, id = id)  
    return render(request, 'detail.html', {'blog' : blog}) 

def update(request, id):
    blog = get_object_or_404(Blog, id = id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'update.html', {'form' : form})

def delete(request, id):
    blog = get_object_or_404(Blog, id = id)
    blog.delete()
    return redirect('read')

def like(request, id):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, id=id)
        if blog.like_user.filter(id=request.user.id).exists():
            blog.like_user.remove(request.user)
        else:
            blog.like_user.add(request.user)
        return redirect('detail', id=id)
    return redirect('login')

def bookmark(request, id):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, id = id)
        if blog.bookmark_user.filter(id = request.user.id).exists():
            blog.bookmark_user.remove(request.user)
        else:
            blog.bookmark_user.add(request.user)
        return redirect('detail', id=id)
    return redirect('login')

def mybookmark(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(bookmark_user=request.user)
        return render(request, 'mybookmark.html', {'blogs' : blogs})
    return redirect('login')