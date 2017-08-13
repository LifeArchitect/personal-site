from urllib.parse import quote_plus
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
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(title__icontains=query)
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, 'blog.html', context)

def post_create(request):
    if not request.staff or not request.user.is_superuser:
        raise Http404

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
    share_string = quote_plus(post.content)
    context = {
        "title": post.title,
        "post": post,
        "share_string": share_string,
    }
    return render(request, 'blog_post.html', context)

def post_update(request, id):
    if not request.staff or not request.user.is_superuser:
        raise Http404

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
    if not request.staff or not request.user.is_superuser:
        raise Http404

    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Successfully Deleted Post")
    return HttpResponseRedirect('/posts/')
