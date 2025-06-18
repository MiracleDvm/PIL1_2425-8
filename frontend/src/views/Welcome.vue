<template>
  <div class="welcome">
    <header class="welcome-header">
      <h1>Bienvenue sur IFRI Comotorage</h1>
      <p>L'application qui connecte conducteurs et passagers pour optimiser vos trajets vers le campus IFRI.</p>
    </header>
    <section class="welcome-actions">
      <router-link to="/login" class="welcome-link login">Se connecter</router-link>
      <router-link to="/register" class="welcome-link register">Créer un compte</router-link>
    </section>
    <section class="welcome-description">
      <h2>Pourquoi IFRI Comotorage ?</h2>
      <p>
        Simplifiez vos déplacements, partagez vos trajets, économisez et faites de nouvelles rencontres grâce à notre plateforme de covoiturage dédiée aux étudiants IFRI.
      </p>
    </section>
  </div>
</template>

<script>
export default {
  name: "Welcome",
};
</script>

<style scoped>
.welcome {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 48px 16px;
  text-align: center;
  background-color: var(--bg-color, #f5f5f5);
  color: var(--text-color, #333);
}
.welcome-header {
  margin-bottom: 32px;
}
.welcome-header h1 {
  font-size: 2.5rem;
  color: var(--primary-color, #3498db);
}
.welcome-header p {
  font-size: 1.2rem;
  margin-top: 10px;
}

.flex_header {
  display: flex;
}
.flex_header img {
  margin: 0 54px;
}
@media screen and (max-width: 544px) {
  .flex_header {
    flex-direction: column;
  }
  .flex_header img {
  margin: auto;
  }
}
  
.welcome-actions {
  margin-bottom: 32px;
  display: flex;
  gap: 24px;
  justify-content: center;
}
.welcome-link {
  display: inline-block;
  padding: 14px 32px;
  border-radius: 6px;
  font-size: 1.1rem;
  font-weight: bold;
  text-decoration: none;
  transition: background 0.2s, color 0.2s;
}
.welcome-link.login {
  background: var(--primary-color, #3498db);
  color: #fff;
}
.welcome-link.login:hover {
  background: #217dbb;
}
.welcome-link.register {
  background: #fff;
  color: var(--primary-color, #3498db);
  border: 2px solid var(--primary-color, #3498db);
}
.welcome-link.register:hover {
  background: var(--primary-color, #3498db);
  color: #fff;
}
.welcome-description {
  max-width: 700px;
  margin-top: 40px;
}
.welcome-description h2 {
  font-size: 2rem;
  margin-bottom: 18px;
}
.welcome-description p {
  font-size: 1.1rem;
  line-height: 1.6;
}
</style>
