from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'about.html', {})

# Blog Posts
def posts_home(request):
    return HttpResponse("<h1>Posts Home</h1>")

def post_create(request):
    return HttpResponse("<h1>Create New Post</h1>")

def post_detail(request):
    return HttpResponse("<h1>Post Detail</h1>")

def post_list(request):
    return HttpResponse("<h1>Post List</h1>")

def post_update(request):
    return HttpResponse("<h1>Update Post</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete Post</h1>")
