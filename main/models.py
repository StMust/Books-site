from django.urls import reverse
from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    author = models.CharField(max_length=100, verbose_name = 'Автор')
    photo = models.ImageField(upload_to ='photos/%m', blank =True, verbose_name='Фото')
    file = models.FileField(upload_to='file/',verbose_name='Книга')
    time_created = models.DateTimeField(auto_now_add = True, verbose_name = 'Время создания')
    time_updated = models.DateTimeField(auto_now = True, verbose_name = 'Последнее время обновления')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name = 'URL')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name = 'Категория')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('show', kwargs={'book_slug' : self.slug })

    
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['-time_created','title']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории', db_index=True)
    slug = models.SlugField(max_length=100, unique = True, db_index = True, verbose_name = 'URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']