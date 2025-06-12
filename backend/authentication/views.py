from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

class PasswordResetRequestView(APIView):
    """
    Permet à un utilisateur de demander la réinitialisation de son mot de passe.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "L'email est requis."}, status=400)
        
        form = PasswordResetForm({"email": email})
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'request': request,
                'token_generator': default_token_generator,
                'email_template_name': 'authentication/password_reset_email.html',  # Utilisation du template personnalisé
            }
            form.save(**opts)
            return Response({"message": "Un lien de réinitialisation a été envoyé à votre adresse email."}, status=200)
        else:
            return Response(form.errors, status=400)

class UtilisateurDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'statut': getattr(user, 'statut', None),
            # Ajoutez d'autres champs si besoin
        })
