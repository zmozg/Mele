from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post_list(request):
    posts_all = Post.published.all()
    paginator = Paginator(posts_all, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = 'blog/post/list.html'
    values = {'posts': posts, 'page': page}
    return render(request, template, values)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    template = 'blog/post/detail.html'
    values = {'post': post}
    return render(request, template, values)
