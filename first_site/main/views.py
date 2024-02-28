from django.shortcuts import render


def index(request):
    return render(request, 'www/index.html')


def category(request, category_slug):
    context = {'slug': category_slug}
    return render(request, 'www/category.html', context)


def detail(request, pk):
    context = {'post': pk}
    return render(request, 'www/detail.html', context)


def all_news(request):
    return render(request, 'www/news_all.html')
