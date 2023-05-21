<template>
  <div class="line-chart">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js/auto";

export default {
  props: {
    data: {
      type: Array,
      required: true,
    },
  },
  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      const canvas = this.$refs.chartCanvas;
      const ctx = canvas.getContext("2d");

      const timestamps = this.data.map((row) => row.timestamp);
      const values = this.data.map((row) => row.value);

      new Chart(ctx, {
        type: "line", // Change type to "line"
        data: {
          labels: timestamps,
          datasets: [
            {
              label: "Stock Value",
              data: values,
            },
          ],
        },
      });
    },
  },
};
</script>

<style>
.line-chart {
  width: 100%;
  height: 400px;
}
</style>
