from django.contrib import admin
from .models import Country, Post, Comment

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'capital']
    search_fields = ['name', 'capital']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'country', 'post_type', 'published_date']
    list_filter = ['post_type', 'country', 'created_date', 'published_date']
    search_fields = ['title', 'content', 'country__name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_date']
    list_filter = ['created_date', 'post']