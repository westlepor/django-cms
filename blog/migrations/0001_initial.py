# Generated by Django 2.1.7 on 2019-02-13 10:14

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ExternalPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField()),
                ('featured_image', models.ImageField(default='', upload_to='', verbose_name='Featured Image')),
                ('url', models.URLField(max_length=100, verbose_name='Blog Post URL')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ExternalPost', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'External Post',
                'verbose_name_plural': 'External Posts',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField()),
                ('content', ckeditor.fields.RichTextField()),
                ('featured_image', models.ImageField(default='', upload_to='', verbose_name='Featured Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Post', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='externalpost',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='Tag'),
        ),
    ]
