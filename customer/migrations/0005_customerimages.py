# Generated by Django 4.0.4 on 2022-09-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_customer_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
