from django.contrib import admin
from django.urls import path, include # Make sure 'include' is here

urlpatterns = [
    path('admin/', admin.site.urls),
    # This connects everything together
    path('api/', include('listings.urls')), 
]