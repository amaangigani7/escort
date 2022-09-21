from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Subscriber)

# class ContactUsAdminConfig(admin.ModelAdmin):
#     list_display = ['name', 'email', 'phone', 'message']
#     readonly_fields=('name', 'email', 'phone', 'message')

# admin.site.register(ContactUs, ContactUsAdminConfig)

admin.site.register(Blog)
admin.site.register(LoveStory)

admin.site.register(PageData)
