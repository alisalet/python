from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Country, Comment
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return redirect('post_list')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def country_posts(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    posts = Post.objects.filter(country=country, published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/country_posts.html', {'country': country, 'posts': posts})

def posts_by_type(request, post_type):
    type_display = dict(Post.POST_TYPE_CHOICES).get(post_type, 'Все посты')
    posts = Post.objects.filter(post_type=post_type, published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/posts_by_type.html', {'posts': posts, 'post_type': post_type, 'type_display': type_display})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(post=post, author=request.user, text=text)
            return redirect('post_detail', pk=post.pk)
    return redirect('post_detail', pk=post.pk)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан! Теперь можно войти.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})