from django.shortcuts import render, get_object_or_404

import blog
from .models import Blog


def blog_list_view(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs,

    }
    return render(request, "home.html", context=context)


def detailview(request, id):
    post = get_object_or_404(Blog, id=id)
    context = {
        "blog": blog,
    }

    return render(request, "blog_detail.html", context=context)