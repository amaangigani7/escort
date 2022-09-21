# Generated by Django 4.0.4 on 2022-09-14 09:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('receiver', models.ManyToManyField(related_name='receiver_liked', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
