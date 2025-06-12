<template>
  <div class="dashboard">
    <h2>Tableau de bord</h2>
    <div v-if="user">
      <p>Bienvenue, {{ user.username }}!</p>
      <p>Email: {{ user.email }}</p>
      <p>Budget Mensuel: {{ user.budget_mensuel }} €</p>
    </div>
    <div v-else>
      <p>Chargement de vos informations...</p>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "Dashboard",
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  created() {
    // Récupère les informations de l'utilisateur dès la création du composant
    this.fetchUser()
  },
  methods: {
    ...mapActions(['fetchUser'])
  }
}
</script>

<style scoped>
.dashboard {
  padding: 20px;
  background-color: var(--bg-color);
  color: var(--text-color);
}

.dashboard h2 {
  color: var(--primary-color);
  margin-bottom: 20px;
}

.dashboard p {
  font-size: 16px;
  margin: 8px 0;
}
</style>
