from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog_detail/<str:slug>/', views.blog_detail, name='blog_detail'),
    path('page_data/<str:slug>/', views.page_data, name='page_data'),
    # path('contact_us_receive/', views.contact_us_receive, name='contact_us_receive'),
]