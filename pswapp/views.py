from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import NewPostForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'about.html', {})

# Blog Posts
def posts_home(request):
    queryset = Post.objects.all().order_by("-timestamp")
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, 'blog.html', context)

def post_create(request):
    new_post = NewPostForm(request.POST or None, request.FILES or None)
    if new_post.is_valid():
        instance = new_post.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/posts/')

    context = {
        "new_post": new_post,
    }
    return render(request, 'new_post.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "title": post.title,
        "post": post,
    }
    return render(request, 'blog_post.html', context)

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    new_post = NewPostForm(request.POST or None, request.FILES or None, instance=post)
    if new_post.is_valid():
        instance = new_post.save(commit=False)
        instance.save()
        messages.success(request, "Edit Successful")
        return HttpResponseRedirect('/posts/')

    context = {
        "title": post.title,
        "post": post,
        "new_post": new_post,
    }
    return render(request, 'new_post.html', context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Successfully Deleted Post")
    return HttpResponseRedirect('/posts/')
