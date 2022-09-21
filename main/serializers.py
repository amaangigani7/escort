from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class LoveStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoveStory
        fields = '__all__'

class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageData
        fields = '__all__'

# class ContactUsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContactUs
#         fields = '__all__'