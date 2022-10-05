from customer.serializers import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions, generics
from rest_framework.response import Response
from customer.models import *
from django.db.models import Q
from .models import *
from .serializers import *


def get_matches():
    return Customer.objects.filter(is_published=True)

@api_view(['GET'])
def matches(request):
    if request.user.is_authenticated:
        profile = Customer.objects.get(user_name=request.user)
        matches = get_matches().filter(is_published=True).filter(
            Q(i_am=profile.looking_for) |
            Q(looking_for=profile.i_am)
        ).exclude(user_name=profile.user_name)
    else:
        matches = get_matches()
    serializer = CustomerSerializer(matches, many=True)
    return Response({'matches': serializer.data})


@api_view(['GET'])
def filtered_matches(request):
    i_am = request.data.get("i_am")
    looking_for = request.data.get("looking_for")
    country = request.data.get("country")
    age_range = request.data.get("age_range").split(' ')
    # breakpoint()
    try:
        matches = get_matches().filter(
            i_am=looking_for, looking_for=i_am, 
            # country=country, 
            age__gte=int(age_range[0]), age__lte=int(age_range[1]))
        if len(matches) < 30:
            from itertools import chain
            more_matches = get_matches().filter(i_am=looking_for, looking_for=i_am).filter(
                Q(country=country) |
                Q(age__gte=int(age_range[0]), age__lte=int(age_range[1]))
            ).exclude(user_name__in=matches)
            matches = list(chain(matches, more_matches))
        serializer = CustomerSerializer(matches, many=True)
        return Response({'matches': serializer.data})
    except Exception as e:
        return Response({"msg": str(e)})


@api_view(['GET'])
def match_detail(request, user_name):
    try:
        match = get_matches().get(user_name=user_name)
        serializer = CustomerSerializer(match)
        return Response({'match_details': serializer.data})
    except Exception as e:
        return Response({"msg": str(e)})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like(request, user_name):
    try:
        match = get_matches().get(user_name=user_name)
        like, created = Like.objects.get_or_create(sender=request.user, to=match)
        if created:
            match.likes_count += 1
            match.save()
            return Response({'msg': "Like sent!"})
        else:
            return Response({'msg': "You have already liked them!"})
    except Exception as e:
        return Response({"msg": str(e)})
    

@api_view(['GET'])
def likes(request):
    try:
        likes = Like.objects.filter(
            Q(sender=request.user) |
            Q(to=request.user))
        serializer = LikeSerializer(likes, many=True)
        return Response({'all_likes': serializer.data})
    except Exception as e:
        return Response({"msg": str(e)})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def review(request, user_name):
    try:
        content = request.data.get("content")
        match = get_matches().get(user_name=user_name)
        review = Review.objects.create(sender=request.user, to=match, content=content)
        msg = "Review Sent!"
        return Response({'msg': msg})
    except Exception as e:
        return Response({"msg": str(e)})

@api_view(['GET'])
def reviews(request):
    try:
        reviews = Review.objects.filter(
            Q(sender=request.user) |
            Q(to=request.user))
        serializer = ReviewSerializer(reviews, many=True)
        return Response({'all_reviews': serializer.data})
    except Exception as e:
        return Response({"msg": str(e)})