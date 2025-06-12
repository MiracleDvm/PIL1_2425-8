import logging
from django.utils.timezone import now

logger = logging.getLogger(__name__)

class PerformanceLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        debut = now()
        response = self.get_response(request)
        fin = now()
        logger.info(f"Requête traitée en {fin - debut} secondes")
        return response
