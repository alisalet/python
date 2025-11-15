from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название страны')
    capital = models.CharField(max_length=100, verbose_name='Столица')
    description = models.TextField(blank=True, verbose_name='Описание страны')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Post(models.Model):
    POST_TYPE_CHOICES = [
        ('culture', 'Культура и традиции'),
        ('city', 'Города и достопримечательности'),
        ('food', 'Национальная кухня'),
        ('advice', 'Советы путешественникам'),
    ]

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна')
    post_type = models.CharField(max_length=20, choices=POST_TYPE_CHOICES, default='city', verbose_name='Тип поста')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name='Главное изображение')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост о путешествии'
        verbose_name_plural = 'Посты о путешествиях'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Комментарий {self.author} к {self.post.title}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_date']