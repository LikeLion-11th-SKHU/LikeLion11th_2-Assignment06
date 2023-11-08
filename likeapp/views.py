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
    already_in_bookmark = bookmark.objects.filter(user=request.user, post=blog).exists() # 현재 사용자가 해당 게시글을 북마크했는지 확인한다.
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
    if request.user.is_authenticated: # 현재 사용자가 인증되어 있는지 확인한다.
        blog = get_object_or_404(Blog, id=id) # 주어진 id에 해당하는 Blog 객체를 가져온다.
        if blog.like_user.filter(id=request.user.id).exists(): # 현재 사용자가 이미 좋아요를 눌렀는지 확인한다.
            blog.like_user.remove(request.user) # 이미 좋아요를 눌렀다면 좋아요를 취소한다.
        else:
            blog.like_user.add(request.user) # 아직 좋아요를 누르지 않았다면 좋아요를 추가한다.
        return redirect('detail', id=id) # 좋아요를 처리한 후에는 detail페이지로 이동한다.
    return redirect('login') # 사용자가 인증되어 있지 않다면 login페이지로 이동한다.

def bookmark(request):
    if request.user.is_authenticated: # 현재 사용자가 인증되어 있는지 확인한다.
        bookmark = request.user.bookmark.all() # 현재 사용자의 모든 북마크를 가져온다.
        return render(request, 'bookmark.html', {'bookmark':bookmark}) # bookmark페이지를 렌더링한다.
    return redirect('login') # 사용자가 인증되어 있지 않다면 login페이지로 이동한다.

