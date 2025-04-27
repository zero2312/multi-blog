from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts} )


def detail(request,id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/detail.html',  {'post': post} )


def about(request):
    return render(request, 'blog/about.html')

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail', id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail', id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create.html', {'form': form})