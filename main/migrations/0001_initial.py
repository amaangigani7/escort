# Generated by Django 4.0.4 on 2022-09-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField(null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-posted_at'],
            },
        ),
        migrations.CreateModel(
            name='LoveStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('image_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'LoveStories',
                'ordering': ['-posted_at'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]