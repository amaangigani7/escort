from django.urls import path
from . import views

urlpatterns = [
    path('matches/', views.matches, name='matches'),
    path('match_detail/<str:user_name>/', views.match_detail, name='match_detail'),
    path('filtered_matches/', views.filtered_matches, name='filtered_matches'),
    path('like/<str:user_name>/', views.like, name='like'),
    path('likes/', views.likes, name='likes'),
    path('review/<str:user_name>/', views.review, name='review'),
    path('reviews/', views.reviews, name='reviews'),
]