import { createRouter, createWebHistory } from 'vue-router';
import Welcome from './views/Welcome.vue';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Dashboard from './views/Dashboard.vue';
import Reservations from './views/Reservations.vue';
import Notifications from './views/Notifications.vue';
import Paiements from './views/Paiements.vue';
import Profile from './views/Profile.vue';
import AdminDashboard from './views/AdminDashboard.vue';
import Register from './views/Register.vue';
import Chat from './components/Chat.vue';
import Trajets from './views/Trajets.vue';
import store from './store';

const routes = [
  { path: '/', component: Welcome },
  { path: '/home', component: Home, meta: { requiresAuth: true } },
  { path: '/login', component: Login, meta: { guestOnly: true } },
  { path: '/register', component: Register, meta: { guestOnly: true } },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/reservations', component: Reservations, meta: { requiresAuth: true } },
  { path: '/trajets', component: Trajets, meta:   { requiresAuth: false } },
  { path: '/chat', component: Chat, meta: { requiresAuth: true } },
  { path: '/notifications', component: Notifications, meta: { requiresAuth: true } },
  { path: '/paiements', component: Paiements, meta: { requiresAuth: true } },
  { path: '/profile', component: Profile, meta: { requiresAuth: true } },
  { path: '/admin', component: AdminDashboard, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!store.state.user;
  if (to.meta && to.meta.guestOnly && isAuthenticated) {
    next('/home');
  } else if (to.meta && to.meta.requiresAuth && !isAuthenticated) {
    next('/');
  } else {
    next();
  }
});

export default router;
