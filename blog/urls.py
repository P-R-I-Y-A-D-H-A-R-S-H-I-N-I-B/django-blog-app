from django.urls import path
from . import views

#this is used to avoid name conflicts with other apps and to make the urls more readable
app_name = "blog"

#urls in the app are defined here (blog/) (blog/post/1) (blog/old_url) (blog/new_url)
urlpatterns = [
    path("", views.index, name="index"), #name is used to refer to the url in the template
    path("post/<str:slug>", views.detail, name="detail"),
    path("old_url", views.old_url_redirect, name="old_url"),
    path("new_url", views.new_url, name="new_page_url") #new_url is the function name in views.py
]

