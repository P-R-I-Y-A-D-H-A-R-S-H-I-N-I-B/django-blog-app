from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging

posts = [
        {'id': 1, 'title': 'Post 1', 'content': 'This is the content of post 1', 'category': 'Sports'},
        {'id': 2,   'title': 'Post 2', 'content': 'This is the content of post 2', 'category': 'Technology'},
        {'id': 3, 'title': 'Post 3', 'content': 'This is the content of post 3', 'category': 'Science'}
    ]

# Create your views here.
def index(request):
    blogs_title = 'Latest Posts'
    page_title = 'Blog'
    return render(request, "blog/index.html", {'blogs_title': blogs_title, 'page_title': page_title, 'posts': posts})

def detail(request, post_id):
    post = next((item for item in posts if item['id'] == post_id), None)
    page_title = 'Blog Post'
    logger = logging.getLogger('TESTING')
    logger.debug(f'post value: {post}')
    return render(request, "blog/detail.html", {'page_title': page_title,'post': post})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url(request):
    return HttpResponse("This is the new url redirect page")
