from django.urls import path
from monitoring.views import PerformanceView

urlpatterns = [
    path("system/", PerformanceView.as_view(), name="system-monitoring"),
]
