from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blog_list(request):
    """Lista de posts del blog"""
    category_filter = request.GET.get('category')
    posts = BlogPost.objects.filter(status='published')
    
    if category_filter:
        posts = posts.filter(category=category_filter)
    
    context = {
        'posts': posts,
        'category_filter': category_filter,
    }
    return render(request, 'public/blog.html', context)


def blog_detail(request, slug):
    """Detalle de un post del blog"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    related_posts = BlogPost.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'public/blog_detail.html', context)
