<template>
  <div class="profile">
    <h2>
      <i class="fas fa-user"></i>
      Mon Profil
    </h2>

    <!-- Message de succès avec animation -->
    <transition name="fade">
      <div v-if="message" class="message success">
        <i class="fas fa-check-circle"></i> {{ message }}
      </div>
    </transition>

    <!-- Message d'erreur avec animation -->
    <transition name="fade">
      <div v-if="error" class="message error">
        <i class="fas fa-exclamation-triangle"></i> {{ error }}
      </div>
    </transition>

    <form @submit.prevent="updateProfile">
      <div class="form-group">
        <label for="email">
          <i class="fas fa-envelope"></i> Email :
        </label>
        <input type="email" id="email" v-model="user.email" disabled />
      </div>

      <div class="form-group">
        <label for="username">
          <i class="fas fa-user-edit"></i> Nom d'utilisateur :
        </label>
        <input type="text" id="username" v-model="user.username" required />
      </div>

      <div class="form-group">
        <label for="statut">
          <i class="fas fa-id-badge"></i> Statut :
        </label>
        <select id="statut" v-model="user.statut" required>
          <option disabled value="">Veuillez sélectionner</option>
          <option value="conducteur">Conducteur</option>
          <option value="passager">Passager</option>
        </select>
      </div>

      <button type="submit" class="btn-save" :disabled="loading">
        <span v-if="loading" class="spinner"></span>
        <span v-else>
          <i class="fas fa-save"></i> Enregistrer
        </span>
      </button>
      <button type="button" class="btn-logout" @click="logout">
        <i class="fas fa-sign-out-alt"></i> Se déconnecter
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Profile",
  data() {
    return {
      user: {
        email: "",
        username: "",
        statut: "",
      },
      message: "",
      error: "",
      loading: false,
    };
  },
  methods: {
    async fetchUserProfile() {
      try {
        const response = await fetch("/api/users/");
        if (response.ok) {
          this.user = await response.json();
        } else {
          this.error = "Impossible de charger le profil utilisateur.";
        }
      } catch (err) {
        console.error("Erreur lors du chargement du profil :", err);
        this.error = "Une erreur est survenue lors du chargement du profil.";
      }
    },
    async updateProfile() {
      this.error = "";
      this.message = "";
      this.loading = true;
      try {
        const response = await fetch("/api/users/", {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.user),
        });
        if (response.ok) {
          this.message = "Profil mis à jour avec succès !";
          // Vous pouvez éventuellement rafraîchir le profil ou réinitialiser des valeurs ici
        } else {
          const data = await response.json();
          this.error = data.error || "Erreur lors de la mise à jour du profil.";
        }
      } catch (err) {
        console.error("Erreur lors de la mise à jour du profil :", err);
        this.error = "Une erreur s'est produite lors de la mise à jour.";
      } finally {
        this.loading = false;
      }
    },
    logout() {
      this.$store.commit('setUser', null);
      this.$router.push('/');
    },
  },
  created() {
    this.fetchUserProfile();
  },
};
</script>

<style scoped>
.profile {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  background-color: var(--bg-color, #ffffff);
  color: var(--text-color, #333333);
  border-radius: 6px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
  color: var(--primary-color, #3498db);
  margin-bottom: 20px;
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #cccccc;
  border-radius: 4px;
}

.btn-save {
  width: 100%;
  padding: 10px;
  background-color: var(--primary-color, #3498db);
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  position: relative;
  font-size: 1rem;
}

.btn-save:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.btn-save:hover:not(:disabled) {
  background-color: var(--secondary-color, #2ecc71);
}

.btn-logout {
  width: 100%;
  padding: 10px;
  background-color: #e74c3c;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 16px;
  font-weight: bold;
  transition: background 0.3s;
}

.btn-logout:hover {
  background-color: #c0392b;
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

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Messages de confirmation/erreur */
.message {
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 4px;
  text-align: center;
}

.message.success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.message.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

/* Transition fade pour messages */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
