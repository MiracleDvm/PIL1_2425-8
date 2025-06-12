import stripe
import requests
from django.conf import settings
from.models import HistoriquePaiement

stripe.api_key = settings.STRIPE_SECRET_KEY

def creer_paiement_stripe(montant, email):
    paiement = stripe.PaymentIntent.create(
        amount=montant * 100,  # montant en centimes
        currency="eur",
        description="Paiement trajet",
        receipt_email=email,
    )
    return paiement.client_secret

def rembourser_paiement_stripe(paiement_id):
    paiement = HistoriquePaiement.objects.get(id=paiement_id)
    remboursement = stripe.Refund.create(payment_intent=paiement.transaction_id)
    paiement.statut = "remboursé"
    paiement.save()
    return remboursement

def rembourser_paiement_paypal(transaction_id):
    headers = {
        "Authorization": f"Bearer {settings.PAYPAL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    url = f"https://api-m.paypal.com/v2/payments/captures/{transaction_id}/refund"
    response = requests.post(url, headers=headers, json={})
    paiement = HistoriquePaiement.objects.get(transaction_id=transaction_id)
    paiement.statut = "remboursé"
    paiement.save()
    return response.json()
