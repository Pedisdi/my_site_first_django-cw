from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader

links = {
    "about": "/about/",
    "about red": "/about/red/",
    "about blue": "/about/blue/",
    "home": "/home/",
    "home red": "/home/red/",
    "home blue": "/home/blue/",
    "contact": "/contact/",
}


def view_color(request, color_type):
    template_name = "color_red.html" if color_type == "red" else "color_blue.html"
    return render(request, template_name)
    # hello world


# def home(request):
#     # print(request.method)
#     return render(request, 'home.html')
def home(request, color_type="white"):
    context = {
        "color_type": color_type,
        "link_name": "about",
        "link": "/about",
        "links": links,
    }
    return render(request, "home.html", context)


def about(request, color_type="white"):
    context = {
        "color_type": color_type,
        "link_name": "about",
        "link": "/about",
        "links": links,
    }
    return render(request, "about.html", context)


def contact(request, color_type="white"):
    context = {
        "color_type": color_type,
        "link_name": "about",
        "link": "/about",
        "links": links,
    }
    return render(request, "contact.html", context)
