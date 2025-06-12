from rest_framework.views import APIView
from rest_framework.response import Response
import psutil

class PerformanceView(APIView):
    def get(self, request):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        return Response({"cpu_usage": cpu, "memory_usage": mem})
