# Generated by Django 4.0.4 on 2022-09-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='about',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
