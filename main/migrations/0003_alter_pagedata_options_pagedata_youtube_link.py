# Generated by Django 4.0.4 on 2022-09-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pagedata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagedata',
            options={'verbose_name_plural': 'Page Data'},
        ),
        migrations.AddField(
            model_name='pagedata',
            name='youtube_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
