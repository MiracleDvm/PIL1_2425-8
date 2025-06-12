// frontend/src/store/mutations.js

export default {
  setUser(state, user) {
    state.user = user;
  },

  setNotifications(state, notifications) {
    state.notifications = notifications;
  },

  // Mutation optionnelle pour supprimer une notification par son ID
  removeNotification(state, notificationId) {
    state.notifications = state.notifications.filter(n => n.id !== notificationId);
  },
}
