# Generated by Django 4.1.1 on 2022-10-05 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0014_rename_adminpanelrequests_adminpanelrequest"),
    ]

    operations = [
        migrations.RemoveField(model_name="adminpanelrequest", name="publish",),
        migrations.RemoveField(model_name="adminpanelrequest", name="verify",),
    ]
