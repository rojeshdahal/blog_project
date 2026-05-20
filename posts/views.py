from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, Post

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