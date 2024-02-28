from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<slug:category_slug>/', category, name='category'),
    path('posts/', all_news, name='posts'),
    path('posts/<int:pk>/', detail, name='post_detail'),
    path('about/',
         TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
]
