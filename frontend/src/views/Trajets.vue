<template>
  <div class="trajet">
    <h2>Détails du Trajet</h2>
    <div class="trajet-card">
      <p><strong>Départ :</strong> {{ trajet.depart }}</p>
      <p><strong>Arrivée :</strong> {{ trajet.arrivee }}</p>
      <p><strong>Date :</strong> {{ formattedDate }}</p>
      <p><strong>Conducteur :</strong> {{ trajet.conducteur }}</p>
      <p><strong>Prix :</strong> {{ trajet.prix }} €</p>
      <!-- Si l'utilisateur est conducteur, proposer les actions de gestion -->
      <div v-if="isConducteur">
        <button class="btn btn-warning me-2" @click="modifierTrajet">
          <i class="bi bi-pencil-square"></i> Modifier
        </button>
        <button class="btn btn-danger" @click="supprimerTrajet">
          <i class="bi bi-trash"></i> Supprimer
        </button>
      </div>
      <!-- Sinon, si l'utilisateur est passager, afficher le bouton de réservation -->
      <div v-else>
        <button class="btn btn-primary" @click="reserver">
          <i class="bi bi-check-lg"></i> Réserver
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Trajet",
  // On attend que le parent transmette currentUser avec le champ "statut"
  props: {
    currentUser: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      // Exemple de données statiques pour le trajet (à adapter en récupérant via API ou store)
      trajet: {
        depart: "Paris",
        arrivee: "Lyon",
        date: "2025-06-20T09:30:00", // format ISO
        conducteur: "Jean Dupont",
        prix: 25,
      }
    };
  },
  computed: {
    // Computed property pour vérifier si l'utilisateur est conducteur
    isConducteur() {
      return this.currentUser.statut === "conducteur";
    },
    // Formate la date de trajet dans un format lisible
    formattedDate() {
      return new Date(this.trajet.date).toLocaleString();
    }
  },
  methods: {
    reserver() {
      // Logique pour réserver le trajet (à remplacer par l'appel API, mise à jour du state, etc.)
      alert("Réservation effectuée pour ce trajet !");
    },
    modifierTrajet() {
      // Logique pour modifier le trajet proposé par le conducteur (redirection vers un formulaire de modification notamment)
      alert("Redirection vers la page de modification du trajet.");
    },
	  supprimerTrajet() {
     // Logique pour supprimer le trajet (appel API, confirmation, etc.)
      if (confirm("Voulez-vous vraiment supprimer ce trajet ?")) {
       alert("Trajet supprimé.");
      }
    }
  }
};
</script>

<style scoped>
.trajet {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
}

.trajet-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.trajet-card p {
  margin: 8px 0;
}

.btn {
  margin-top: 15px;
}

/** */
.trajet h2 {
  margin: 21px;
  color: #3498db;
}
/** */
</style>

