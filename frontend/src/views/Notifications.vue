<template>
  <div class="notifications">
    <h2>
      <i class="fas fa-bell"></i> Notifications
    </h2>
    <transition-group name="list" tag="div" class="notification-list">
      <div
        v-for="notification in notifications"
        :key="notification.id"
        class="notification-item"
      >
        <div class="notification-content">
          <p>{{ notification.message }}</p>
          <small>{{ formatDate(notification.date) }}</small>
        </div>
        <button class="dismiss-btn" @click="dismiss(notification.id)">
          <i class="fas fa-times"></i>
        </button>
      </div>
    </transition-group>
    <div v-if="notifications.length === 0" class="empty">
      <i class="fas fa-info-circle"></i> Aucune notification.
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Notifications',
  computed: {
    ...mapState({
      notifications: state => state.notifications, // supposant que notifications se trouve dans le state Vuex
    }),
  },
  created() {
    // Récupération des notifications dès la création du composant
    this.fetchNotifications();
  },
  methods: {
    ...mapActions(['fetchNotifications']),
    /**
     * Supprime une notification avec son identifiant.
     */
    dismiss(notificationId) {
      // Cette mutation doit être définie dans votre store pour retirer la notification.
      this.$store.commit('removeNotification', notificationId);
    },
    /**
     * Formate une date pour une présentation lisible.
     */
    formatDate(date) {
      return new Date(date).toLocaleString();
    },
  },
};
</script>

<style scoped>
.notifications {
  max-width: 600px;
  margin: 20px auto;
  padding: 15px;
  background-color: var(--bg-color, #f9f9f9);
  border-radius: 8px;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.1);
}

.notifications h2 {
  text-align: center;
  color: var(--primary-color, #3498db);
  margin-bottom: 20px;
}

.notification-list {
  display: flex;
  flex-direction: column;
}

.notification-item {
  display: flex;
  align-items: center;
  background: #fff;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 4px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.notification-item:hover {
  background-color: #f1f1f1;
}

.notification-content {
  flex-grow: 1;
}

.notification-content p {
  margin: 0;
  font-size: 1rem;
}

.notification-content small {
  display: block;
  color: #999;
  margin-top: 4px;
}

.dismiss-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  color: #e74c3c;
  font-size: 1.2rem;
  padding: 5px;
  transition: color 0.3s ease;
}

.dismiss-btn:hover {
  color: #c0392b;
}

.empty {
  text-align: center;
  padding: 20px;
  color: #777;
  font-style: italic;
}

/* Transition pour les notifications (entrée/sortie) */
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
