# Generated by Django 4.0.4 on 2022-09-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_i_am_customer_looking_for_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
