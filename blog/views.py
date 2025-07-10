from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from blog.models import Post
from django.core.paginator import Paginator
from blog.forms import ContactForm
from django.core.mail import send_mail

#this is static data
# posts = [
#         {'id': 1, 'title': 'Post 1', 'content': 'This is the content of post 1', 'category': 'Sports'},
#         {'id': 2,   'title': 'Post 2', 'content': 'This is the content of post 2', 'category': 'Technology'},
#         {'id': 3, 'title': 'Post 3', 'content': 'This is the content of post 3', 'category': 'Science'}
#     ]

# Create your views here.
def index(request):
    blogs_title = 'Latest Posts'
    page_title = 'Blog'

    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "blog/index.html", {'blogs_title': blogs_title, 'page_title': page_title, 'post_obj': page_obj})

def detail(request, slug: str):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post not found")
    
    page_title = 'Blog Post'
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)
    logger = logging.getLogger('TESTING')
    logger.debug(f'post value: {post}')
    return render(request, "blog/detail.html", {'page_title': page_title,'post': post, 'related_posts': related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url(request):
    return HttpResponse("This is the new url redirect page")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            success_message = 'Your message has been sent successfully'
            #write code to send email
            # send_mail(
            #     'New message from your blog',
            #     f'Name: {name}\nEmail: {email}\nMessage: {message}',
            #     email,
            #     [email],
            # )
            return render(request, "blog/contact.html", {'page_title': 'Contact', 'form': form, 'success_message': success_message})
        else:
            logger = logging.getLogger('TESTING')
            logger.debug(f'Form is not valid: {form.errors}')
        return render(request, "blog/contact.html", {'page_title': 'Contact', 'form': form, 'name': name, 'email': email, 'message': message})
            # return HttpResponse(f'Name: {name}, Email: {email}, Message: {message}')
    return render(request, "blog/contact.html", {'page_title': 'Contact'})