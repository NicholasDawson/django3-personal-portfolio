from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def all_blogs(request):
    count = BlogPost.objects.count()
    posts = BlogPost.objects.order_by('-date')[:5]  # This sorts the blog posts by the date field
    return render(request, 'blog/all_blogs.html', {'posts': posts, 'count': count})


def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
