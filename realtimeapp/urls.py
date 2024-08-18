# realtimeapp/urls.py (or main project urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stocks.urls')),
    # Add other app URLs as needed
]
