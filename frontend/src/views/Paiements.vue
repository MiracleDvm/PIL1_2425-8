<template>
  <div>
    <h2>Historique des paiements</h2>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Montant</th>
          <th>Méthode</th>
          <th>Statut</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="paiement in paiements" :key="paiement.id">
          <td>{{ paiement.date_paiement }}</td>
          <td>{{ paiement.montant }} €</td>
          <td>{{ paiement.methode_paiement }}</td>
          <td>{{ paiement.statut }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return { paiements: [] };
  },
  mounted() {
    fetch("/api/paiements/")
      .then(response => response.json())
      .then(data => (this.paiements = data));
  },
};
</script>
