<template>
  <nav class="navbar">
    <router-link to="/" class="nav-link">Présentation</router-link>
    <router-link to="/home" class="nav-link">Accueil</router-link>
    <router-link to="/trips" class="nav-link">Trajets</router-link>
    <router-link to="/reservations" class="nav-link">Réservations</router-link>
    <router-link to="/notifications" class="nav-link">Notifications</router-link>
    <router-link to="/profile" class="nav-link">Profil</router-link>
    <router-link to="/login" class="nav-link">Connexion</router-link>
    <router-link to="/register" class="nav-link">Inscription</router-link>
  </nav>
</template>

<style>
.navbar {
    display: flex;
    justify-content: space-around;
    background: var(--primary-color, #3498db);
    padding: 15px;
    border-radius: 8px;
}

.nav-link {
    color: white;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease-in-out;
}

.nav-link:hover {
    color: #ffd700;
}
</style>
