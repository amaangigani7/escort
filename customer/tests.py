from django.test import TestCase

# Create your tests here.
import random
from customer.models import *
import datetime
from faker import Faker
fake = Faker()
from django.utils import timezone



for i in range(500):
    print(i)
    try:
        Customer.objects.create(
            full_name=fake.name(), 
            email=fake.email(), 
            user_name=fake.user_name(), 
            dob=datetime.datetime.now(),
            i_am="Male",
            looking_for="Female",
            city=fake.city(), 
            country=fake.country(),
            is_active=True)
    except:
        print("skipped this one.")