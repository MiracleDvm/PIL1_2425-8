import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class ErrorHandlingMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error(f"Erreur détectée: {exception}")
        return None
