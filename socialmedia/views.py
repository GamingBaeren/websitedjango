from django.shortcuts import render, get_object_or_404
from .models import BlogPost, SocialMediaLink
from django.core.paginator import Paginator

def blog_list(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'socialmedia/blog_list.html', {'page_obj': page_obj})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'socialmedia/blog_detail.html', {'post': post})

def socialmedia_main(request):
    links = SocialMediaLink.objects.all()
    return render(request, 'socialmedia/socialmedia_main.html', {'links': links})
