from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def subscribe(request):
    try:
        email = request.data.get('email')
        if "." in email and '@' in email:
            subcribe, created = Subscriber.objects.get_or_create(email=email)
            if created == False:
                return Response({'msg': 'You are already subscribed'})
            else:
                return Response({'msg': 'Your email has been added to the subscriber list'})
        else:
            return Response({'msg': "Your email is not valid"})
    except:
        return Response({'msg': "Email could not be registered!"})


@api_view(['POST'])
def unsubscribe(request):
    email = request.data.get('email')
    try:
        subcriber = Subscriber.objects.get(email=email)
        subcriber.delete()
        return Response({'msg': 'You have been unsubscribed'})
    except:
        return Response({'msg': "No subscription found to unsubscribe"})

@api_view(['GET'])
def blogs(request):
    try:
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response({'all_blogs': serializer.data})
    except Exception as e:
        return Response({"msg": str(e)})


@api_view(['GET'])
def blog_detail(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        serializer = BlogSerializer(blog)
        return Response({'blog_details': serializer.data})
    except Exception as e:
        return Response({"msg": str(e)})

@api_view(['GET'])
def page_data(request, slug):
    try:
        data = PageData.objects.get(slug=slug)
        serializer = PageDataSerializer(data)
        return Response({'page_data': serializer.data})
    except Exception as e:
        return Response({"msg": str(e)})

# @api_view(['POST'])
# def contact_us_receive(request):
#     # breakpoint()
#     name = request.data.get('name')
#     email = request.data.get('email')
#     phone = request.data.get('phone')
#     message = request.data.get('message')
#     # try:
#     cu = ContactUs.objects.create(name=name, email=email, phone=phone, message=message)
#     msg = "Request has been sent"
#     serializer = ContactUsSerializer(cu)
#     return Response({'msg': msg, 'request': serializer.data})
