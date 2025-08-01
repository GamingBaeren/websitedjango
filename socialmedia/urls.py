from django.urls import path
from . import views

app_name = 'socialmedia'

urlpatterns = [
    path('', views.socialmedia_main, name='socialmedia_main'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
