# Generated by Django 3.1.14 on 2022-04-12 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%m', verbose_name='Фото')),
                ('file', models.FileField(upload_to='file/', verbose_name='Книга')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='Последнее время обновления')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книги',
                'ordering': ['-time_created', 'title'],
            },
        ),
    ]
