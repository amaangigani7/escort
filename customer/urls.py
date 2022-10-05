from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from django.views.decorators.csrf import csrf_exempt

app_name = 'customer'

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refreshtoken'),
    path('verify/<auth_token>/', views.verify , name="verify"),
    path('user_details/', views.user_details , name='user_details'),
    path('forgot_password/' , views.forgot_password , name="forgot_password"),
    path('change_password/<token>/' , views.change_password , name="change_password"),
    # # path('your_account/', views.your_account, name='your_account'),
    path('user_details/edit/', views.user_details_edit, name='user_details_edit'),
    path('apply_for_verification/', views.apply_for_verification, name='apply_for_verification'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)