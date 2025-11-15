from .models import Country, Post

def blog_context(request):
    return {
        'countries': Country.objects.all(),
        'post_types': Post.POST_TYPE_CHOICES,
    }