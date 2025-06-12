<template>
  <div class="home">
    <header class="home-header">
      <h1>Bienvenue, {{ username }} !</h1>
      <p>Ravi de vous retrouver sur IFRI Comotorage.</p>
    </header>
    <section class="quick-actions">
      <h2>Actions rapides</h2>
      <div class="actions-list">
        <router-link to="/trips" class="action-card">
          <span>Voir les trajets disponibles</span>
        </router-link>
        <router-link to="/trips/create" class="action-card">
          <span>Proposer un trajet</span>
        </router-link>
        <router-link to="/reservations" class="action-card">
          <span>Mes réservations</span>
        </router-link>
        <router-link to="/chat" class="action-card">
          <span>Messagerie</span>
        </router-link>
        <router-link to="/profile" class="action-card">
          <span>Mon profil</span>
        </router-link>
      </div>
    </section>
    <section class="project-description">
      <h2>À propos</h2>
      <p>
        IFRI Comotorage facilite le covoiturage entre étudiants grâce à un système de mise en relation intelligent, une messagerie instantanée et un suivi de paiements sécurisé.
      </p>
    </section>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      username: "Utilisateur", // À remplacer par le nom réel de l'utilisateur connecté
    };
  },
  mounted() {
    // TODO: Récupérer le vrai nom de l'utilisateur connecté si disponible
  },
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px;
  text-align: center;
  background-color: var(--bg-color, #f5f5f5);
  color: var(--text-color, #333);
}

.home-header {
  margin-bottom: 30px;
}

.home-header h1 {
  font-size: 2.5rem;
  color: var(--primary-color, #3498db);
}

.home-header p {
  font-size: 1.2rem;
  margin-top: 10px;
}

.quick-actions {
  margin-bottom: 32px;
}

.quick-actions h2 {
  font-size: 1.5rem;
  margin-bottom: 16px;
}

.actions-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}

.action-card {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 180px;
  min-height: 60px;
  padding: 16px 24px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  color: var(--primary-color, #3498db);
  font-weight: bold;
  text-decoration: none;
  font-size: 1.1rem;
  transition: box-shadow 0.2s, background 0.2s;
}

.action-card:hover {
  background: var(--primary-color, #3498db);
  color: #fff;
  box-shadow: 0 4px 16px rgba(52, 152, 219, 0.15);
}

.project-description {
  max-width: 800px;
  margin-top: 40px;
}

.project-description h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.project-description p {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 30px;
}
</style>
