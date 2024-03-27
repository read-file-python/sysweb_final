from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.utils import timezone

from .models import Post

TODAY = timezone.now()
ITEMS_POST_HOME = 5


def index(request):
    posts = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=TODAY
    )[:ITEMS_POST_HOME]
    context = {'posts': posts}
    return render(request, 'www/index.html', context)


def category(request, category_slug):
    posts = get_list_or_404(
        Post.objects.select_related(
            'category', 'location', 'author'
        ),
        is_published=True,
        category__slug=category_slug,
        pub_date__lte=TODAY,
        category__is_published=True
    )

    context = {'post_list': posts}
    return render(request, 'www/category.html', context)


def detail(request, pk):
    post = get_object_or_404(
        Post,
        id=pk,
        pub_date__lte=TODAY,
        is_published=True,
        category__is_published=True
    )

    context = {'post': post}
    return render(request, 'www/detail.html', context)


def all_news(request):
    posts = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=TODAY
    )
    context = {'posts': posts}
    return render(request, 'www/news_all.html', context)

