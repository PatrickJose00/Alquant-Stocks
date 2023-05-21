<script setup>
defineProps({
  items: {
    type: Object,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
});
const headers = [
  "Cumulative Return",
  "Annualized Return",
  "Annualized Volatility",
];
</script>

<template>
  <h2 class="table-title">{{ title }}</h2>
  <table class="boring-table">
    <thead>
      <tr>
        <th v-for="header in headers" :key="header">
          {{ header }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in items" :key="item.id">
        <td>
          {{ item.cumulative_return }}
        </td>
        <td>
          {{ item.annualized_return }}
        </td>
        <td>{{ item.annualized_volatility }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped lang="scss">
.table-title {
  margin: 30px 0 0 0;
}
.boring-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  font-family: sans-serif;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
.boring-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}

.boring-table th,
.boring-table td {
  padding: 12px 15px;
}

.boring-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.boring-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.boring-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.boring-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}
</style>
