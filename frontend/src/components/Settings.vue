<template>
  <div class="settings">
    <h2>Personnalisation</h2>
    <button @click="toggleTheme" class="btn-theme">🌙 / ☀️ Mode</button>
    <input type="color" v-model="selectedColor" @change="applyColor" />
  </div>
</template>

<script>
export default {
  data() {
    return { isDarkMode: false, selectedColor: "#3498db" };
  },
  mounted() {
    this.isDarkMode = localStorage.getItem("darkMode") === "true";
    document.documentElement.classList.toggle("dark-mode", this.isDarkMode);
  },
  methods: {
    toggleTheme() {
      this.isDarkMode = !this.isDarkMode;
      localStorage.setItem("darkMode", this.isDarkMode);
      document.documentElement.classList.toggle("dark-mode", this.isDarkMode);
    },
    applyColor() {
      document.documentElement.style.setProperty("--primary-color", this.selectedColor);
      localStorage.setItem("primaryColor", this.selectedColor);
    }
  }
};
</script>

<style>
.settings {
    padding: 20px;
    background: var(--bg-color, #f5f5f5);
    border-radius: 8px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.btn-theme {
    padding: 10px;
    cursor: pointer;
    background-color: var(--primary-color, #3498db);
    color: white;
    border: none;
    border-radius: 5px;
}

.dark-mode {
    background-color: #121212;
    color: #ffffff;
}
</style>
