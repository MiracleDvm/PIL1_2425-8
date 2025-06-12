<template>
  <div>
    <h2>Surveillance du système</h2>
    <p>Utilisation CPU: {{ system.cpu_usage }}%</p>
    <p>Utilisation mémoire: {{ system.memory_usage }}%</p>
  </div>
</template>

<script>
export default {
  data() {
    return { system: {} };
  },
  mounted() {
    fetch("/api/system/")
      .then(response => response.json())
      .then(data => (this.system = data));
  },
};
</script>
