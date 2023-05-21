<template>
  <div class="container">
    <h1>Stocks Page {{ $route.params.symbol }}</h1>
    <ChartDataProvider
      :symbol="$route.params.symbol"
      v-slot="{ data, loading }"
    >
      <LineChart :data="data" v-if="!loading" />
    </ChartDataProvider>
    <TableDataProvider
      :symbol="$route.params.symbol"
      v-slot="{ data, loading }"
    >
      <StatisticsTable :items="data" v-if="!loading" title="Stock Statistics" />
    </TableDataProvider>
  </div>
</template>

<script setup>
import StatisticsTable from "@/components/StatisticsTable.vue";
import LineChart from "@/components/LineChart.vue";
import TableDataProvider from "@/services/TableDataProvider.vue";
import ChartDataProvider from "@/services/ChartDataProvider.vue";
</script>

<style scoped lang="scss">
.container {
  max-width: 960px;
  margin-right: auto;
  margin-left: auto;
  display: flex;
  justify-content: center;
  flex-direction: column;
}
</style>
