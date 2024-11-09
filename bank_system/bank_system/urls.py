# bank_system/urls.py (main project URL config)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Customer.urls')),  # Include your app’s URLs here
]