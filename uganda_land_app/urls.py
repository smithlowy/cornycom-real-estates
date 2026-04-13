from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings  # Added this
from django.conf.urls.static import static  # Added this

def home(request):
    return HttpResponse("Cornycom Real Estates API is Running! To see data, go to /api/plots/")

urlpatterns = [
    path('', home), 
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')), 
]

# --- ADD THIS AT THE VERY BOTTOM ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)