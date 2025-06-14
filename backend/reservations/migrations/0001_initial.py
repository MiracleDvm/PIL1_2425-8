# Generated by Django 3.2.25 on 2025-06-11 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('en attente', 'En attente'), ('confirmé', 'Confirmé'), ('annulé', 'Annulé')], default='en attente', max_length=15)),
                ('passager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trajet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trajet')),
            ],
        ),
    ]
