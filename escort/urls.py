from django.contrib import admin
from django.urls import path, include

admin.site.site_header  =  "Admin Login"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('customer.urls')),
    path("", include("main.urls")),
    path("", include("match.urls"))
]
