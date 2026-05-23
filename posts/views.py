from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, Post
from django.http import HttpResponseForbidden

from .models import Post


def post_list(request):

    posts = Post.objects.all()

    return render(request, "posts/post_list.html", {
        "posts": posts
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    return render(request, "posts/post_detail.html", {
        "post": post
    })

@login_required
def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect('post_list')

    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {
        'form': form
    })

@login_required
def edit_post(request, id):

    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == "POST":

        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

            return redirect('post_detail', id=post.id)

    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {
        'form': form
    })

@login_required
def delete_post(request, id):

    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == "POST":
        post.delete()

        return redirect('post_list')

    return render(request, 'posts/delete_post.html', {
        'post': post
    })