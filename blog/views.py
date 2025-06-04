from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('detail', id=post.id)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


def about(request):
    return render(request, 'blog/about.html')


@login_required
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


@login_required
def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.author != request.user:
        return redirect('detail', id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail', id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create.html', {'form': form})


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.author != request.user:
        return redirect('detail', id=post.id)

    if request.method == 'POST':
        post.delete()
        return redirect('blog-home')

    return render(request, 'blog/delete_post.html', {'post': post})


@login_required
def comment_edit(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if comment.author != request.user:
        return redirect('detail', id=comment.post.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('detail', id=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form})


@login_required
def comment_delete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if comment.author != request.user:
        return redirect('detail', id=comment.post.id)

    if request.method == 'POST':
        comment.delete()
        return redirect('detail', id=comment.post.id)

    return render(request, 'blog/delete_comment.html', {'comment': comment})
