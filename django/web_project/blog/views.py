from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog

data = {
    'blogs': [
        {
            'id': 1,
            'title': 'Programming From the Scratch',
            'image': '1.jpg',
            'is_active': True,
            'is_home': False,
            'description': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime, eos cum ipsa quisquam quasi'
        },
        {
            'id': 2,
            'title': 'Python Web Development Tutorial',
            'image': '4.jpg',
            'is_active': True,
            'is_home': True,
            'description': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime, eos cum ipsa'
        },
        {
            'id': 3,
            'title': 'Django Tutorial',
            'image': '2.png',
            'is_active': False,
            'is_home': True,
            'description': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime, eos'
        },
        {
            'id': 4,
            'title': 'React for Beginners',
            'image': '3.png',
            'is_active': True,
            'is_home': True,
            'description': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime, eos cum ipsa quisquam quasi aut eius numquam'
        }
    ]
}


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


def blog_details(request, id):
    blog =  Blog.objects.get(id=id)
    return render(request, "blog/blog-details.html", {'blog':blog})
