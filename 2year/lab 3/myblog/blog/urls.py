from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from . import views


def catch_all(request, unknown_path):
    return render(request, 'blog/404.html', status=404)


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('country/<int:country_id>/', views.country_posts, name='country_posts'),
    path('type/<str:post_type>/', views.posts_by_type, name='posts_by_type'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),

    path('<path:unknown_path>/', catch_all),
]