<template>
  <div class="register-page">
    <h2>S'inscrire</h2>
    <transition name="fade">
      <div v-if="error" class="error">{{ error }}</div>
    </transition>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">Nom d'utilisateur :</label>
        <input
          type="text"
          id="username"
          v-model="username"
          placeholder="Votre nom d'utilisateur"
          required
        />
      </div>
      <div class="form-group">
        <label for="email">Email :</label>
        <input
          type="email"
          id="email"
          v-model="email"
          placeholder="Votre email"
          required
        />
      </div>
      <!-- Sélection du statut -->
      <div class="form-group">
        <label for="statut">Statut :</label>
        <select id="statut" v-model="statut" required>
          <option disabled value="">Veuillez sélectionner</option>
          <option value="conducteur">Conducteur</option>
          <option value="passager">Passager</option>
        </select>
      </div>
      <div class="form-group">
        <label for="password">Mot de passe :</label>
        <input
          type="password"
          id="password"
          v-model="password"
          placeholder="Votre mot de passe"
          required
        />
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirmer le mot de passe :</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="confirmPassword"
          placeholder="Confirmez votre mot de passe"
          required
        />
      </div>
      <button type="submit" class="btn-register" :disabled="loading">
        <span v-if="loading" class="spinner"></span>
        <span v-else>S'inscrire</span>
      </button>
    </form>
    <p>
      Vous avez déjà un compte ?
      <router-link to="/login">Connectez-vous</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      statut: "",
      error: "",
      loading: false,
    };
  },
  methods: {
    async handleRegister() {
      this.error = "";
      if (this.password !== this.confirmPassword) {
        this.error = "Les mots de passe ne correspondent pas.";
        return;
      }
      this.loading = true;
      try {
        const response = await fetch("/api/auth/register/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password,
            statut: this.statut,
          }),
        });
        const data = await response.json();
        if (response.ok) {
          this.$router.push("/login");
        } else {
          this.error = data.error || "Erreur lors de l'inscription.";
        }
      } catch (err) {
        console.error("Erreur lors de l'inscription :", err);
        this.error = "Une erreur est survenue. Veuillez réessayer.";
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.register-page {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  background-color: var(--bg-color, #ffffff);
  color: var(--text-color, #333333);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h2 {
  color: var(--primary-color, #3498db);
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #cccccc;
  border-radius: 4px;
}

.btn-register {
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

.btn-register:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.btn-register:hover:not(:disabled) {
  background-color: var(--secondary-color, #2ecc71);
}

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

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.error {
  color: #e74c3c;
  margin-bottom: 10px;
  font-weight: bold;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
