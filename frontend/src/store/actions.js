// frontend/src/store/actions.js

export default {
  async fetchUser({ commit }) {
    try {
      const response = await fetch('/api/users/');
      const data = await response.json();
      commit('setUser', data);
    } catch (error) {
      console.error("Erreur lors du fetch de l'utilisateur :", error);
    }
  },

  async fetchNotifications({ commit }) {
    try {
      const response = await fetch('/api/notifications/');
      const data = await response.json();
      commit('setNotifications', data);
    } catch (error) {
      console.error("Erreur lors du fetch des notifications :", error);
    }
  },

  // Exemple d'action pour mettre à jour le profil utilisateur
  async updateUser({ commit }, payload) {
    try {
      const response = await fetch('/api/users/', {
        method: 'PUT',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      if(response.ok) {
        const data = await response.json();
        commit('setUser', data);
      } else {
        console.error("Erreur lors de la mise à jour de l'utilisateur");
      }
    } catch (error) {
      console.error("Erreur lors de la mise à jour de l'utilisateur :", error);
    }
  },
}
