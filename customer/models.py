from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify


# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError(gettext_lazy('You must enter an email'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Super User must have "is_staff=True"')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Super User must have "is_superuser=True"')
        return self.create_user(email, user_name, password, **other_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    gender_choices = (("Male", "Male"), ("Female", "Female"))

    email = models.EmailField(gettext_lazy('email_address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=150, null=True)
    mobile_number = PhoneNumberField(blank=True, null=True, unique=True)
    about = models.TextField(gettext_lazy('about'), max_length=500, blank=True, null=True)
    dob = models.DateTimeField(null=True, blank=True)
    i_am = models.CharField(max_length=255, choices=gender_choices, null=True)
    looking_for = models.CharField(max_length=255, choices=gender_choices, null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True)
    hair_color = models.CharField(max_length=100, null=True, blank=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    sexual_orientation = models.CharField(max_length=100, null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    # other_info = models.TextField(blank=True, null=True)

    likes_count = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    forget_password_token = models.CharField(max_length=100, blank=True, null=True)
    

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name',]

    @property
    def get_image_url(self):
        image_obj = self.customerimage
        image_urls = []
        image_urls.append(image_obj)
        return image_urls

    @property
    def like_details(self):
        lis = []
        for i in self.receiver_liked.all():
            lis.append({"user_name": i.user_name, "email": i.email})
        return self.receiver_liked.all()

    def __str__(self):
        return self.user_name

class CustomerImage(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)
    img_1 = models.TextField(null=True, blank=True)
    img_2 = models.TextField(null=True, blank=True)
    img_3 = models.TextField(null=True, blank=True)
    img_4 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.customer.user_name

class AdminPanelRequest(models.Model):
    req_type_choices = (("Publish", "Publish"), ("Verification", "Verification"))
    
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    req_type = models.CharField(max_length=255, choices=req_type_choices, default="Publish")
    # verify = models.BooleanField(default=False)
    # publish = models.BooleanField(default=False)    

    img_1 = models.TextField(null=True, blank=True)
    img_2 = models.TextField(null=True, blank=True)
    img_3 = models.TextField(null=True, blank=True)
    img_4 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.customer.user_name+ "  -  " + self.req_type
    



