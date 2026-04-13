from django.urls import path
from .views import PlotListAPIView

urlpatterns = [
    # This must match what your Flet app is calling
    path('plots/', PlotListAPIView.as_view(), name='plot-list'),
]