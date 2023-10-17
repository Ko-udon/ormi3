from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def postlist(request):
    posts = Post.objects.all()
    return render(request, 'tube/postlist.html', {'posts':posts})

def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                post = post,
                message = form.cleaned_data['message'],
                author = request.user
            )
            c.save()

    return render(request, 'tube/postdetail.html', {'post':post, 'form':form})

def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact = tag)
    return render(request,'tube/postlist.html', {'posts':posts})

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('postdetail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'tube/create.html', {'form':form})

@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('postlist')
    else:
        form = PostForm(instance=post)
    return render(request, 'tube/create.html', {'form': form})

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('postlist')
    return render(request, 'tube/delete.html', {'post': post})
