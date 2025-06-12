<template>
  <div class="reservations">
    <h2>
      <i class="fas fa-calendar-check"></i> Mes Réservations
    </h2>
    <transition-group name="list" tag="div" class="reservation-list">
      <div
        v-for="reservation in reservations"
        :key="reservation.id"
        class="reservation-item"
      >
        <div class="reservation-info">
          <p><strong>Réservation :</strong> {{ reservation.title }}</p>
          <p>
            <strong>Date :</strong>
            {{ formatDate(reservation.date) }}
          </p>
          <p><strong>Statut :</strong> {{ reservation.status }}</p>
        </div>
        <button class="cancel-btn" @click="cancelReservation(reservation.id)" :disabled="loadingIds.includes(reservation.id)">
          <i class="fas fa-times-circle"></i>
          <span v-if="!loadingIds.includes(reservation.id)">Annuler</span>
          <span v-else class="spinner"></span>
        </button>
      </div>
    </transition-group>
    <div v-if="reservations.length === 0" class="empty">
      <i class="fas fa-info-circle"></i> Aucune réservation.
    </div>
  </div>
</template>

<script>
export default {
  name: "Reservations",
  data() {
    return {
      reservations: [],
      loadingIds: [], // tableau des id de réservations en cours d'annulation
      error: ""
    };
  },
  created() {
    this.fetchReservations();
  },
  methods: {
    async fetchReservations() {
      try {
        const response = await fetch("/api/reservations/");
        if (response.ok) {
          this.reservations = await response.json();
        } else {
          this.error = "Erreur lors du chargement des réservations.";
        }
      } catch (err) {
        console.error("Erreur :", err);
        this.error = "Une erreur est survenue lors du chargement des réservations.";
      }
    },
    formatDate(date) {
      return new Date(date).toLocaleString();
    },
    async cancelReservation(reservationId) {
      if (!confirm("Voulez-vous vraiment annuler cette réservation ?")) return;
      this.loadingIds.push(reservationId);
      try {
        const response = await fetch(`/api/reservations/${reservationId}/`, {
          method: "DELETE",
        });
        if (response.ok) {
          this.reservations = this.reservations.filter(r => r.id !== reservationId);
        } else {
          alert("Erreur lors de l'annulation de la réservation.");
        }
      } catch (err) {
        console.error("Erreur lors de l'annulation :", err);
        alert("Une erreur est survenue lors de l'annulation de la réservation.");
      } finally {
        this.loadingIds = this.loadingIds.filter(id => id !== reservationId);
      }
    }
  }
};
</script>

<style scoped>
.reservations {
  max-width: 700px;
  margin: 30px auto;
  padding: 20px;
  background-color: var(--bg-color, #f9f9f9);
  color: var(--text-color, #333);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.reservations h2 {
  text-align: center;
  color: var(--primary-color, #3498db);
  margin-bottom: 20px;
}

.reservation-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.reservation-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff;
  padding: 15px;
  border-radius: 4px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.05);
  transition: background 0.3s ease;
}

.reservation-item:hover {
  background-color: #f1f1f1;
}

.reservation-info p {
  margin: 3px 0;
  font-size: 0.95rem;
}

.cancel-btn {
  background: transparent;
  border: none;
  color: #e74c3c;
  font-size: 1.1rem;
  cursor: pointer;
  padding: 5px 8px;
  transition: color 0.3s ease;
  display: flex;
  align-items: center;
}

.cancel-btn:hover {
  color: #c0392b;
}

.cancel-btn:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

/* Spinner Loader (pour le bouton d'annulation) */
.spinner {
  width: 18px;
  height: 18px;
  border: 3px solid #e74c3c;
  border-top: 3px solid rgba(0, 0, 0, 0.2);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Message vide */
.empty {
  text-align: center;
  padding: 20px;
  color: #777;
  font-style: italic;
}

/* Transition pour la liste */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
