from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.forms import TextInput, Textarea
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)

class CustomerAdminConfig(UserAdmin):
    model = Customer
    search_fields = ('email', 'user_name', 'full_name', "i_am", "looking_for")
    list_filter = ('is_active', 'is_staff', 'is_verified', 'is_published', "i_am", "looking_for")
    ordering = ('-created_at',)
    list_display = ('email', 'user_name', 'full_name', "i_am", "likes_count", "age", 
                    'is_active', 'is_staff', 'is_verified', 'is_published')
    readonly_fields=('verification_token', 'forget_password_token', 'created_at')

    fieldsets = (
        (None, {'fields':
            ('email', 'user_name', 'full_name', "i_am", "looking_for", "dob", "age", "city",
            "country", "height", "weight", "sexual_orientation", "languages", "hair_color", "likes_count")
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verified', 'is_published')}),
        ('Personal', {'fields': ('created_at', 'verification_token', 
                    'forget_password_token')})
    )

    # formfield_overrides = {
    #     Customer.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'full_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Customer, CustomerAdminConfig)
admin.site.register(CustomerImage)
admin.site.register(AdminPanelRequest)