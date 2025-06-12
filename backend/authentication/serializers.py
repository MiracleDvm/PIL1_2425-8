from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'statut', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    # Ajout du champ statut, avec choix provenant du modèle personnalisé.
    statut = serializers.ChoiceField(choices=User.STATUT_CHOICES, default=User.PASSAGER)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'statut']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            statut=validated_data.get('statut', User.PASSAGER)
        )
        return user
