import { createStore } from 'vuex';

function loadUser() {
  try {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  } catch {
    return null;
  }
}

export default createStore({
  state: {
    user: loadUser(),
    notifications: [],
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
      if (user) {
        localStorage.setItem('user', JSON.stringify(user));
      } else {
        localStorage.removeItem('user');
      }
    },
    setNotifications(state, notifications) {
      state.notifications = notifications;
    },
  },
  actions: {
    fetchUser({ commit }) {
      fetch("/api/user/")
        .then(response => response.json())
        .then(data => commit("setUser", data));
    },
    fetchNotifications({ commit }) {
      fetch("/api/notifications/")
        .then(response => response.json())
        .then(data => commit("setNotifications", data));
    },
  },
});
