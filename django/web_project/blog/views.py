from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog


def index(request):
    context = {
        'blogs': Blog.objects.filter(is_active=True, is_home=True)
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        'blogs': Blog.objects.filter(is_active=True)
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, slug):
    blog =  Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {'blog':blog})
