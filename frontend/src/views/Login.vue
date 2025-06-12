<template>
  <div class="login-page">
    <h2>Se connecter</h2>
    <transition name="fade">
      <div v-if="error" class="error">{{ error }}</div>
    </transition>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="email">Email :</label>
        <input type="email" id="email" v-model="email" placeholder="Votre email" required />
      </div>
      <div class="form-group">
        <label for="password">Mot de passe :</label>
        <input type="password" id="password" v-model="password" placeholder="Votre mot de passe" required />
      </div>
      <div class="form-group remember-me">
        <input type="checkbox" id="rememberMe" v-model="rememberMe" />
        <label for="rememberMe">Se souvenir de moi</label>
      </div>
      <button type="submit" class="btn-login" :disabled="loading">
        <span v-if="loading" class="spinner"></span>
        <span v-else>Se connecter</span>
      </button>
    </form>
    <p>
      Vous n'avez pas de compte ?
      <router-link to="/register">Inscrivez-vous</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      rememberMe: false,
      error: "",
      loading: false,
    };
  },
  methods: {
    async handleLogin() {
      this.error = "";
      this.loading = true;
      try {
        const response = await fetch("/api/auth/login/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: this.email, password: this.password }),
        });
        if (!response.ok) {
          this.error = "Identifiants invalides. Veuillez réessayer.";
          this.loading = false;
          return;
        }
        const user = await response.json();
        this.$store.commit("setUser", user);
        this.loading = false;
        this.$router.push("/home");
      } catch (err) {
        this.error = err.message || "Erreur lors de la connexion";
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
/* Container principal */
.login-page {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  background-color: var(--bg-color, #ffffff);
  color: var(--text-color, #333333);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

/* Titre */
h2 {
  color: var(--primary-color, #3498db);
  margin-bottom: 20px;
}

/* Groupes de formulaires */
.form-group {
  margin-bottom: 15px;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input[type="email"],
.form-group input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #cccccc;
  border-radius: 4px;
}

/* "Remember me" */
.remember-me {
  display: flex;
  align-items: center;
}

.remember-me input[type="checkbox"] {
  margin-right: 8px;
}

/* Bouton login */
.btn-login {
  width: 100%;
  padding: 10px;
  background-color: var(--primary-color, #3498db);
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  position: relative;
}

.btn-login:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.btn-login:hover:not(:disabled) {
  background-color: var(--secondary-color, #2ecc71);
}

/* Spinner Loader */
.spinner {
  width: 18px;
  height: 18px;
  border: 3px solid #fff;
  border-top: 3px solid rgba(0, 0, 0, 0.2);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  display: inline-block;
  vertical-align: middle;
}

/* Animation pour le spinner */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Message d'erreur */
.error {
  color: #e74c3c;
  margin-bottom: 10px;
  font-weight: bold;
}

/* Transition fade pour le message error */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
