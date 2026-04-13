from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# This function creates a simple message for the home page (the empty '')
def home(request):
    return HttpResponse("Cornycom Real Estates API is Running! To see data, go to /api/plots/")

urlpatterns = [
    # 1. The Home Page
    path('', home), 

    # 2. The Admin Panel
    path('admin/', admin.site.urls),

    # 3. Your Listings API (CRITICAL: Keep this line!)
    path('api/', include('listings.urls')), 
]