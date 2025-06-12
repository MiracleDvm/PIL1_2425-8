from django.http import JsonResponse

def custom_error_handler(request, exception):
    return JsonResponse({"error": "Une erreur s'est produite.", "message": str(exception)}, status=500)
